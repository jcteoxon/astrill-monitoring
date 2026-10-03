import json
from datetime import datetime
from zoneinfo import ZoneInfo

FILE = "astrill account.json"

today = datetime.now(
    ZoneInfo("Asia/Manila")
).date()

with open(FILE, "r", encoding="utf-8") as f:
    data = json.load(f)

for account in data:
    expiry = datetime.strptime(
        account["expiry_date"],
        "%Y-%m-%d"
    ).date()

    account["days_remaining"] = max(
        (expiry - today).days,
        0
    )

with open(FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

print("Days remaining updated")
