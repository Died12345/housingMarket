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
