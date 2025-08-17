import time
from ingest import fetch_earthquake_data
from process import filter_event, extract_event_data
from db import store_event

while True:
    events = fetch_earthquake_data()
    for event in events:
        if filter_event(event):
            data = extract_event_data(event)
            store_event(data)
            print(f"Stored: {data['location']} - Mag {data['magnitude']}")
    time.sleep(300)  # Run every 5 minutes