from pymongo import MongoClient

client = MongoClient("mongodb://mongodb:27017")

db = client["movies_db"]
movie_collection = db["movies"]
