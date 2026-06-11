from datetime import datetime
from zoneinfo import ZoneInfo
import sys

country = sys.argv[1]

country_timezone = {
    "India": "Asia/Kolkata",
    "Japan": "Asia/Tokyo",
    "Germany": "Europe/Berlin",
    "USA": "America/New_York"
}

timezone = country_timezone.get(country)

if timezone:
    current_time = datetime.now(
        ZoneInfo(timezone)
    ).strftime("%Y-%m-%d %H:%M:%S")

    print(f"{country} -> {current_time}")

    with open(f"{country}.txt", "w") as f:
        f.write(f"{country} -> {current_time}")
else:
    print(f"Timezone not found for {country}")
