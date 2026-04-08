from fastapi import APIRouter
from schemas.movie_schema import Movie
from services import movie_service

router = APIRouter(prefix="/movies", tags=["Movies"])

@router.post("/")
def create(movie: Movie):
    return movie_service.create_movie(movie)

@router.get("/")
def list_movies():
    return movie_service.get_movies()

@router.get("/{movie_id}")
def get(movie_id: str):
    return movie_service.get_movie(movie_id)

@router.put("/{movie_id}")
def update(movie_id: str, movie: Movie):
    return movie_service.update_movie(movie_id, movie)

@router.delete("/{movie_id}")
def delete(movie_id: str):
    return movie_service.delete_movie(movie_id)
