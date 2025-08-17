import requests
from config import USGS_API_URL, INDIA_BOUNDS
from datetime import datetime

def fetch_earthquake_data():
    params = {
        "format": "geojson",
        "starttime": datetime.utcnow().strftime("%Y-%m-%d"),
        **INDIA_BOUNDS
    }
    response = requests.get(USGS_API_URL, params=params)
    return response.json().get("features", [])