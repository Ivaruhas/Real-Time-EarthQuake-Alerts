from pymongo import MongoClient
from config import MONGO_URI, DB_NAME, COLLECTION_NAME

client = MongoClient(MONGO_URI)
collection = client[DB_NAME][COLLECTION_NAME]

def store_event(event_data):
    if not collection.find_one({"timestamp": event_data["timestamp"]}):
        collection.insert_one(event_data)

def get_all_events():
    return list(collection.find())