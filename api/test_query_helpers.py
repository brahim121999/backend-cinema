from database import SessionLocal
from query_helpers import *
from datetime import datetime

db = SessionLocal()

# test get_movie
movie = get_movie(db,1)
print(movie.title,movie.genres)

# test get_movies
movies = get_movies(db,5)
for movie in movies:
    print(f"ID :{movie.movieId}, Titre : {movie.title}, Genre: {movie.genres}")

# test get_rating
rating = get_rating(db,1,1)
print(rating.userId, rating.movieId, rating.rating, datetime.fromtimestamp(rating.timestamp).strftime('%Y-%m-%d %H:%M:%S'))

db.close()