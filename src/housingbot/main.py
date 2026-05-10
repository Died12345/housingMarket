import time

from dotenv import load_dotenv

from .config import DB_PATH, DEFAULT_FILTERS, Filters
from .db import connect, filter_new, mark_seen
from .models import Listing
from .notify import send_listings
from .sources import funda, pararius, vesteda

SOURCES = [pararius, funda, vesteda]


def collect(filters: Filters) -> list[Listing]:
    all_listings: list[Listing] = []
    for source in SOURCES:
        for city in filters.cities:
            try:
                got = source.scrape(city, filters.max_rent, filters.min_bedrooms)
                print(f"[{source.NAME}] {city}: {len(got)} listings")
                all_listings.extend(got)
            except Exception as exc:
                print(f"[{source.NAME}] {city}: FAILED - {exc}")
            time.sleep(2)
    return all_listings


def run(filters: Filters = DEFAULT_FILTERS) -> None:
    load_dotenv()
    listings = collect(filters)
    conn = connect(DB_PATH)
    try:
        new_only = filter_new(conn, listings)
        print(f"new since last run: {len(new_only)}")
        send_listings(new_only)
        mark_seen(conn, listings)
    finally:
        conn.close()


if __name__ == "__main__":
    run()
