# Bootstrap prompt for local Claude Code

Copy everything below the `---` line into your local Claude Code session running on your Windows laptop. It's a single self-contained prompt that recreates the whole project from scratch — no need to clone the GitHub branch.

---

You are setting up a Dutch rental scraper project on this Windows machine. Read this whole brief, then build it. Don't ask me clarifying questions — every decision below is final.

## Who I am

BI specialist (~7 years, currently at Midux). Stack: Qlik Sense, Power BI, SQL/T-SQL. Side venture FusionCraft (B2B outbound, n8n + Supabase + Claude API). Comfortable with Python and JS. On Windows (ASUS VivoBook S16), PowerShell. Prefer terse technical answers over hand-holding. Code style: functional > OO unless state genuinely belongs in a class, type hints in Python, pydantic for data contracts at boundaries, comments explain why not what, `uv` for envs, `ruff` for lint.

## Goal

Hunt for a 1-2 bed rental in the Utrecht-Amsterdam corridor:

- I commute to Utrecht by car (current job)
- My girlfriend will commute to Amsterdam by train (when she lands a job, soon)
- Budget: €1,500/month all-in (= ~€1,300 kale rent + €150 service + €150 utilities)
- Move-in: ASAP / next 1-2 months
- My gross: €5,750/month ex 8% vakantiegeld → €74,520/yr → qualifies solo at every common landlord rule (3.5×, 4×, even strict 4×-base-only)

Target cities, ranked by car-to-Utrecht commute:

- **Amersfoort** (primary — 20-25 min A28, ~35 min train to A'dam)
- **Almere** (cheapest stock, 40-55 min A27 to Utrecht)
- **Nijkerk** (smaller, 25-30 min A28)
- **Leusden, Soest, Weesp** (backups)

Skip: Hilversum/Bussum/Naarden (Gooi premium blows budget), Veenendaal (kills her future commute), sociale huur (8+ year waiting lists).

## Deliverables

1. A Python project (`uv` managed) at the current working directory.
2. A scraper module that pulls listings from Pararius, Funda, and Vesteda for the target cities under €1,300 kale rent, dedupes via SQLite, and pings new listings to a Telegram bot.
3. A notes file at `notes/YYYY-MM-DD-rental-search-utrecht-amsterdam.md` (use today's date) documenting the search thesis.
4. After files are written, run `uv sync`, then run a Telegram-only smoke test, then run the scraper once to seed the dedupe DB.

## Tech decisions (already made — don't second-guess)

- **TLS impersonation via `curl_cffi` + `chrome120` fingerprint**, not vanilla `httpx`. Pararius, Funda, Huurwoningen.nl, Vesteda all return 403 to plain HTTP fetchers due to Cloudflare. `curl_cffi` is ~2 MB and gets through without Playwright's 200 MB overhead.
- HTML parsing with `beautifulsoup4` + `lxml`.
- Dedupe in SQLite via stdlib `sqlite3` — keyed on `(source, listing_id)`.
- Notifier: Telegram bot (Markdown, web preview disabled, 4000-char chunking).
- Config via `pydantic` model + `python-dotenv` for the `.env`.
- If a site eventually starts blocking `curl_cffi`, swap that single source module to Playwright — the rest of the pipeline stays the same.

## File tree to create

```
.
├── .env.example
├── .gitignore
├── pyproject.toml
├── notes/2026-MM-DD-rental-search-utrecht-amsterdam.md   # use today's date
├── output/.gitkeep
└── src/housingbot/
    ├── __init__.py
    ├── config.py
    ├── db.py
    ├── main.py
    ├── models.py
    ├── notify.py
    └── sources/
        ├── __init__.py
        ├── funda.py
        ├── pararius.py
        └── vesteda.py
```

## File contents

### `pyproject.toml`

```toml
[project]
name = "housingbot"
version = "0.1.0"
description = "Daily rental listing scraper: Utrecht (car) + Amsterdam (train) commute zone"
requires-python = ">=3.11"
dependencies = [
    "curl-cffi>=0.7",
    "beautifulsoup4>=4.12",
    "lxml>=5.0",
    "httpx>=0.27",
    "pydantic>=2.5",
    "python-dotenv>=1.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/housingbot"]

[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "I", "B", "UP", "SIM"]
```

### `.env.example`

```
# Telegram bot for new-listing pings.
# Setup:
#   1. Open Telegram, message @BotFather, /newbot, follow prompts -> grab the TOKEN.
#   2. Message your new bot at least once (any text) - or just message @userinfobot to get your chat_id directly.
#   3. Open https://api.telegram.org/bot<TOKEN>/getUpdates -> grab "chat":{"id":...}.
TELEGRAM_BOT_TOKEN=
TELEGRAM_CHAT_ID=
```

### `.gitignore`

```
.env
.venv/
__pycache__/
*.pyc
*.egg-info/
output/*.sqlite
output/*.sqlite-journal
.uv/
.ruff_cache/
```

### `output/.gitkeep`

Empty file.

### `src/housingbot/__init__.py`

Empty file.

### `src/housingbot/models.py`

```python
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
```

### `src/housingbot/config.py`

```python
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
```

### `src/housingbot/db.py`

```python
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
```

### `src/housingbot/notify.py`

```python
import os

import httpx

from .models import Listing

TELEGRAM_MAX = 4000


def telegram_send(text: str) -> None:
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID")
    if not (token and chat_id):
        print("[notify] TELEGRAM_* env not set, printing instead:\n" + text)
        return
    resp = httpx.post(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data={
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "Markdown",
            "disable_web_page_preview": "true",
        },
        timeout=15,
    )
    resp.raise_for_status()


def format_listing(listing: Listing) -> str:
    bits = [f"*{listing.title}*", f"{listing.city.title()} - EUR {listing.rent_eur}/mo"]
    if listing.bedrooms:
        bits.append(f"{listing.bedrooms} bed")
    if listing.sqm:
        bits.append(f"{listing.sqm} m2")
    bits.append(f"[{listing.source}]({listing.url})")
    return " - ".join(bits)


def send_listings(listings: list[Listing]) -> None:
    if not listings:
        return
    header = f"{len(listings)} new rental listing(s)\n\n"
    body = "\n\n".join(format_listing(listing) for listing in listings)
    msg = header + body
    for start in range(0, len(msg), TELEGRAM_MAX):
        telegram_send(msg[start : start + TELEGRAM_MAX])
```

### `src/housingbot/sources/__init__.py`

Empty file.

### `src/housingbot/sources/pararius.py`

```python
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
```

### `src/housingbot/sources/funda.py`

```python
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
    """Funda rentals for one city. If curl_cffi 403s here for >2 days, swap to Playwright."""
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
```

### `src/housingbot/sources/vesteda.py`

```python
import re

from bs4 import BeautifulSoup
from curl_cffi import requests

from ..models import Listing

BASE = "https://www.vesteda.com"
NAME = "vesteda"


def scrape(city: str, max_rent: int, min_bedrooms: int = 1) -> list[Listing]:
    """Vesteda institutional listings - regulated rents, most likely to fit budget."""
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
```

### `src/housingbot/main.py`

```python
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
```

### `notes/<TODAY>-rental-search-utrecht-amsterdam.md`

Use today's date in the filename. Content should cover, in this order:

1. **Constraints recap** (budget €1,500 all-in, no city, car-to-Utrecht for me, train-to-Amsterdam for her, 1-2 bed, ASAP).
2. **Budget reality check.** All-in €1,500 ≈ kale €1,150-1,300 after €150 service + €150-200 utilities. Mention the *Wet betaalbare huur* (in force since 1 July 2024) capping rent via the points system (WWS) up to ~€1,158/mo kale, with a middenhuur band above. Source: https://www.rijksoverheid.nl/onderwerpen/woningmarkt/wet-betaalbare-huur. The cheap stock is on institutional landlord portals, not the big aggregators.
3. **Geography shortlist** as a markdown table with columns: Town | Car → Utrecht (rush) | Train → A'dam Centraal | €1,500 realism | Notes. Rows for Amersfoort (best balance), Almere (cheapest, worst car commute), Nijkerk (wildcard), Lelystad (only if budget breaks), Veenendaal (skip), Hilversum/Bussum/Naarden (out of budget — Gooi premium), Weesp (best for her, mediocre for me).
4. **Recommendation:** 1) Amersfoort primary, 2) Almere backup, 3) Nijkerk wildcard.
5. **Where to search** in tiers: institutional (Vesteda, Bouwinvest, MVGM, Heimstaden) → aggregators (Pararius, Funda, Huurwoningen.nl) → local/regional (Rebo Groep, Domica, Facebook groups) → ignore (sociale huur).
6. **Income verdict.** Gross €5,750 + 8% vakantiegeld = €6,210/mo equivalent. Qualifies solo at 3.5× (cap €1,774), 4× incl. holiday (cap €1,552), even 4× base only (cap €1,437). No guarantor needed.
7. **Live snapshot validation** (web-search 2026-05-10): Almere city avg €1,615, but Stedenwijk avg €1,498 and Centrum Almere Buiten avg €1,340 — confirms €1,300 kale is real stock there. Reference live listings: John Coltranestraat 2-bed/89 m² €1,185, Poseidonsingel 2-bed/72 m² €945. Sociale huur 2026 cap: €932,93. Anti-bot reality: Pararius/Funda/Huurwoningen.nl/Vesteda all 403 vanilla HTTP — that's why the scraper uses curl_cffi.
8. **Workflow for 1-2 month timeline.** Daily monitoring (24-72h listing lifespan). Pre-built application packet: 3 payslips, werkgeversverklaring, ID, bank statement, brief letter explaining her job-hunt situation. Viewing strategy: respond within an hour, take first slot, decide on the spot.
9. **Scraper section** documenting setup, run, schedule (Windows Task Scheduler every 30 min, or PowerShell `loop.ps1`), filters location (`src/housingbot/config.py`), and known limits (anti-bot evolves; if a source consistently 403s, swap that module to Playwright).
10. **Open actions:** set up Telegram bot, register manually on Vesteda/Bouwinvest/Heimstaden (they rank by registration date), revisit shortlist with empirical scraper data after 3-4 days.

Keep prose tight and scannable. Cite URLs for factual claims.

## Setup commands to run after writing files

```powershell
# 1. Install uv if missing
where.exe uv 2>$null
if (-not $?) {
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    Write-Host "Restart PowerShell, then re-run me."
    exit
}

# 2. Install deps
uv sync

# 3. Wire up the .env
copy .env.example .env
Write-Host "Open .env and paste TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID, then continue."
notepad .env
```

After I close notepad, run a Telegram-only smoke test:

```powershell
uv run python -c "from dotenv import load_dotenv; load_dotenv(); from housingbot.notify import telegram_send; telegram_send('housingbot test ping')"
```

If I get the test ping in Telegram, run the scraper once to seed the dedupe DB:

```powershell
uv run python -m housingbot.main
```

Expected stdout pattern:
```
[pararius] amersfoort: N listings
[pararius] almere: N listings
...
new since last run: <count>
```

## Done when

- All files exist with the exact content above.
- `uv sync` completes without error.
- The Telegram smoke-test ping arrives in my chat.
- The first scraper run produces a non-empty Telegram message (or a clear `FAILED - HTTP 403` per source if anti-bot blocks my residential IP — in that case, tell me which source(s) failed and I'll decide whether to switch to Playwright).

## What to do if you hit obstacles

- `curl_cffi` install fails on Windows: it usually means missing Visual C++ redistributables. Suggest installing `vc_redist.x64.exe` from Microsoft and retrying `uv sync`.
- All sources return 403: my residential IP is blocked. Don't try to "fix" by adding more headers — switch the affected source(s) to Playwright (`uv add playwright && uv run playwright install chromium`) and rewrite the source module using `playwright.sync_api.sync_playwright()`.
- `uv sync` succeeds but `uv run` can't find Python: PATH issue, restart PowerShell.
- Selectors return 0 listings (HTTP 200 but empty parse): site HTML changed. Tell me the URL and I'll re-derive selectors against a fetched HTML sample.

Don't ask me what to do mid-flight on these — just attempt the suggested fix, and if it doesn't work in one try, surface the error with full traceback so I can decide.
