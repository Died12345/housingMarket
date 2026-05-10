import sqlite3
from pathlib import Path

from .models import Listing

SCHEMA = """
CREATE TABLE IF NOT EXISTS seen (
    source TEXT NOT NULL,
    listing_id TEXT NOT NULL,
    title TEXT,
    city TEXT,
    rent_eur INTEGER,
    bedrooms INTEGER,
    sqm INTEGER,
    url TEXT,
    first_seen TEXT NOT NULL DEFAULT (datetime('now')),
    PRIMARY KEY (source, listing_id)
);
"""


def connect(db_path: Path) -> sqlite3.Connection:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.executescript(SCHEMA)
    return conn


def filter_new(conn: sqlite3.Connection, listings: list[Listing]) -> list[Listing]:
    new: list[Listing] = []
    for listing in listings:
        cur = conn.execute(
            "SELECT 1 FROM seen WHERE source = ? AND listing_id = ?",
            (listing.source, listing.listing_id),
        )
        if cur.fetchone() is None:
            new.append(listing)
    return new


def mark_seen(conn: sqlite3.Connection, listings: list[Listing]) -> None:
    rows = [
        (
            listing.source,
            listing.listing_id,
            listing.title,
            listing.city,
            listing.rent_eur,
            listing.bedrooms,
            listing.sqm,
            listing.url,
        )
        for listing in listings
    ]
    conn.executemany(
        "INSERT OR IGNORE INTO seen "
        "(source, listing_id, title, city, rent_eur, bedrooms, sqm, url) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        rows,
    )
    conn.commit()
