import requests
from datetime import time
from itertools import zip_longest
from src.bus_data.models import Arrival

import json

res = requests.get("http://localhost:7341/api/v1/arrivals?stop=5128&stop=2057")
res.raise_for_status()

data = res.json()
print(json.dumps(data, indent=2))

e1_stop = []
e2_stop = []

# data is a dict where keys are stop IDs
for stop_id, stop_info in data.items():
    stop_name = stop_info.get("stop_name", "Unknown")

    for item in stop_info.get("arrivals", []):
        arrival = Arrival(
            route=item["route"],
            headsign=item["headsign"],
            agency=item["agency"],
            scheduled_arrival=item["scheduled_arrival"],
            real_time_arrival=item.get(
                "real_time_arrival"
            ),  # .get() in case it's missing
            stop_id=stop_id,
            stop_name=stop_name,
        )
        if arrival.route == "133":
            print("skipping")
            continue
        if arrival.stop_id == "5128":
            e1_stop.append(arrival)
        elif arrival.stop_id == "2057":
            e2_stop.append(arrival)

# sort by arrival time
e1_stop.sort(key=lambda x: x.minutes_until)
e2_stop.sort(key=lambda x: x.minutes_until)


print("-----------------------------------------------------------")
# First, find the longest string to determine column width
all_texts = []
temp_list = []
for e1, e2 in zip_longest(e1_stop, e2_stop, fillvalue=None):
    if e1:
        minutes = f"{e1.minutes_until:2d}"  # Right-align minutes in 2 spaces
        e1_text = f"[{e1.route}] {minutes}mins {e1.display_time or e1.scheduled_display_time or 'N/A'}"
    else:
        e1_text = "[---] N/A"

    if e2:
        minutes = f"{e2.minutes_until:2d}"  # Right-align minutes in 2 spaces
        e2_text = f"[{e2.route}] {minutes}mins {e2.display_time or e2.scheduled_display_time or 'N/A'}"
    else:
        e2_text = "[---] N/A"

    temp_list.append((e1_text, e2_text))
    all_texts.extend([e1_text, e2_text])

max_width = max(len(text) for text in all_texts) + 2  # Add padding

# Now print with dynamic width
for e1_text, e2_text in temp_list:
    print(f"{e1_text:<{max_width}} | {e2_text:<{max_width}}")


input("press <Enter> to exit...")
