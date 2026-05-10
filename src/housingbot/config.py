from pathlib import Path

from pydantic import BaseModel


class Filters(BaseModel):
    cities: list[str]
    max_rent: int
    min_bedrooms: int = 1


# Defaults aligned with the search thesis: kale rent <= ~€1,300 lands ~€1,500 all-in.
# Cities ranked by car-to-Utrecht commute, with Almere as the budget option.
DEFAULT_FILTERS = Filters(
    cities=["amersfoort", "almere", "nijkerk", "leusden", "soest", "weesp"],
    max_rent=1300,
    min_bedrooms=1,
)

DB_PATH = Path("output/housingbot.sqlite")
