import re

from bs4 import BeautifulSoup
from curl_cffi import requests

from ..models import Listing

BASE = "https://www.funda.nl"
NAME = "funda"


def _parse_int(text: str) -> int | None:
    m = re.search(r"(\d[\d.,]*)", text or "")
    if not m:
        return None
    return int(m.group(1).replace(".", "").replace(",", ""))


def scrape(city: str, max_rent: int, min_bedrooms: int = 1) -> list[Listing]:
    """Funda rentals for one city. Funda hardens against scraping more often than
    Pararius; if curl_cffi starts returning 403, swap to Playwright headless."""
    url = f"{BASE}/zoeken/huur?selected_area=%5B%22{city.lower()}%22%5D&price=%220-{max_rent}%22"
    resp = requests.get(
        url,
        impersonate="chrome120",
        timeout=25,
        headers={"Accept-Language": "nl-NL,nl;q=0.9,en;q=0.8"},
    )
    if resp.status_code != 200:
        raise RuntimeError(f"funda {city}: HTTP {resp.status_code}")

    soup = BeautifulSoup(resp.text, "lxml")
    out: list[Listing] = []

    cards = soup.select("[data-test-id='search-result-item']") or soup.select(
        "div.flex.flex-col.gap-3.p-4"
    )
    for card in cards:
        a = card.select_one("a[data-testid='object-link']") or card.select_one(
            "a[href*='/huur/']"
        )
        if not a:
            continue
        href = a.get("href", "")
        title = a.get_text(" ", strip=True).split("\n")[0]
        price_el = card.find(
            string=re.compile(r"€\s?\d[\d.,]*\s?(p/?m|per maand|/mnd)?", re.IGNORECASE)
        )
        price_text = (price_el or "").strip()
        rent = _parse_int(price_text) or 0

        full_url = BASE + href if href.startswith("/") else href
        listing_id = href.rstrip("/").split("/")[-1] or full_url
        out.append(
            Listing(
                source=NAME,
                listing_id=listing_id,
                title=title,
                city=city,
                rent_eur=rent,
                bedrooms=None,
                sqm=None,
                url=full_url,
                raw_price_text=price_text,
            )
        )
    return out
