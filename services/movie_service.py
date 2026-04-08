from repositories import movie_repository

def create_movie(movie):
    return movie_repository.create_movie(movie.dict())

def get_movies():
    return movie_repository.get_movies()

def get_movie(movie_id):
    return movie_repository.get_movie(movie_id)

def update_movie(movie_id, movie):
    return movie_repository.update_movie(movie_id, movie.dict())

def delete_movie(movie_id):
    return movie_repository.delete_movie(movie_id)
