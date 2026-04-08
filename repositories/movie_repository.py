from database import movie_collection
from bson import ObjectId

def create_movie(movie: dict):
    result = movie_collection.insert_one(movie)
    return str(result.inserted_id)

def get_movies():
    movies = []
    for movie in movie_collection.find():
        movie["_id"] = str(movie["_id"])
        movies.append(movie)
    return movies

def get_movie(movie_id: str):
    movie = movie_collection.find_one({"_id": ObjectId(movie_id)})
    if movie:
        movie["_id"] = str(movie["_id"])
    return movie

def update_movie(movie_id: str, data: dict):
    movie_collection.update_one(
        {"_id": ObjectId(movie_id)},
        {"$set": data}
    )
    return get_movie(movie_id)

def delete_movie(movie_id: str):
    movie_collection.delete_one({"_id": ObjectId(movie_id)})
    return {"message": "Filme deletado"}
