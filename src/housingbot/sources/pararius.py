import re

from bs4 import BeautifulSoup
from curl_cffi import requests

from ..models import Listing

BASE = "https://www.pararius.com"
NAME = "pararius"


def _parse_int(text: str) -> int | None:
    m = re.search(r"(\d[\d.,]*)", text or "")
    if not m:
        return None
    return int(m.group(1).replace(".", "").replace(",", ""))


def scrape(city: str, max_rent: int, min_bedrooms: int = 1) -> list[Listing]:
    """Pararius listings for one city. Returns kale-rent listings under max_rent."""
    url = f"{BASE}/apartments/{city.lower()}/0-{max_rent}/{min_bedrooms}-bedrooms"
    resp = requests.get(
        url,
        impersonate="chrome120",
        timeout=20,
        headers={"Accept-Language": "nl-NL,nl;q=0.9,en;q=0.8"},
    )
    if resp.status_code != 200:
        raise RuntimeError(f"pararius {city}: HTTP {resp.status_code}")

    soup = BeautifulSoup(resp.text, "lxml")
    out: list[Listing] = []
    for card in soup.select("section.listing-search-item"):
        a = card.select_one("a.listing-search-item__link--title")
        if not a:
            continue
        href = a.get("href", "")
        title = a.get_text(strip=True)
        price_el = card.select_one(".listing-search-item__price")
        price_text = price_el.get_text(strip=True) if price_el else ""
        rent = _parse_int(price_text) or 0

        sqm: int | None = None
        bedrooms: int | None = None
        for li in card.select(".illustrated-features__item"):
            txt = li.get_text(" ", strip=True)
            low = txt.lower()
            if "m²" in txt or "m2" in low:
                sqm = _parse_int(txt)
            elif "slaapkamer" in low or "bedroom" in low:
                bedrooms = _parse_int(txt)

        full_url = BASE + href if href.startswith("/") else href
        out.append(
            Listing(
                source=NAME,
                listing_id=href.rstrip("/").split("/")[-1] or full_url,
                title=title,
                city=city,
                rent_eur=rent,
                bedrooms=bedrooms,
                sqm=sqm,
                url=full_url,
                raw_price_text=price_text,
            )
        )
    return out
