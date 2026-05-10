import re

from bs4 import BeautifulSoup
from curl_cffi import requests

from ..models import Listing

BASE = "https://www.vesteda.com"
NAME = "vesteda"


def _parse_int(text: str) -> int | None:
    m = re.search(r"(\d[\d.,]*)", text or "")
    if not m:
        return None
    return int(m.group(1).replace(".", "").replace(",", ""))


def scrape(city: str, max_rent: int, min_bedrooms: int = 1) -> list[Listing]:
    """Vesteda institutional listings. Their site renders cards server-side, so
    a single request usually returns the full set for a city."""
    url = f"{BASE}/nl/woningaanbod?placeOfResidences%5B%5D={city.title()}"
    resp = requests.get(
        url,
        impersonate="chrome120",
        timeout=20,
        headers={"Accept-Language": "nl-NL,nl;q=0.9,en;q=0.8"},
    )
    if resp.status_code != 200:
        raise RuntimeError(f"vesteda {city}: HTTP {resp.status_code}")

    soup = BeautifulSoup(resp.text, "lxml")
    out: list[Listing] = []
    for card in soup.select("article, .property-card, [class*='ObjectCard']"):
        a = card.select_one("a[href*='/woning/'], a[href*='/property/']")
        if not a:
            continue
        href = a.get("href", "")
        title = card.get_text(" ", strip=True)[:120]
        price_match = re.search(r"€\s?([\d.,]+)", card.get_text(" ", strip=True))
        rent = int(price_match.group(1).replace(".", "").replace(",", "")) if price_match else 0
        if rent and rent > max_rent:
            continue
        full_url = BASE + href if href.startswith("/") else href
        out.append(
            Listing(
                source=NAME,
                listing_id=href.rstrip("/").split("/")[-1] or full_url,
                title=title,
                city=city,
                rent_eur=rent,
                bedrooms=None,
                sqm=None,
                url=full_url,
                raw_price_text=price_match.group(0) if price_match else "",
            )
        )
    return out
