from dataclasses import dataclass


@dataclass(frozen=True)
class Listing:
    source: str
    listing_id: str
    title: str
    city: str
    rent_eur: int
    bedrooms: int | None
    sqm: int | None
    url: str
    raw_price_text: str = ""
