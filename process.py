def filter_event(event):
    mag = event['properties']['mag']
    return mag and mag >= 4.5

def extract_event_data(event):
    return {
        "type": "earthquake",
        "location": event['properties']['place'],
        "magnitude": event['properties']['mag'],
        "latitude": event['geometry']['coordinates'][1],
        "longitude": event['geometry']['coordinates'][0],
        "timestamp": event['properties']['time']
    }