# %%
from database import SessionLocal
from models import Movie, Rating, Tag, Link

db = SessionLocal()

# Get some films
movies = db.query(Movie).limit(10).all()

for movie in movies:
    print(f"ID : {movie.movieId}, Titre : {movie.title}, Genres : {movie.genres}")

#  Get action films
action_movies = db.query(Movie).filter(Movie.genres.like("%Action%")).limit(5).all()

for movie in action_movies:
   print(f"ID : {movie.movieId}, Titre : {movie.title}, Genres : {movie.genres}")


# Get ratings
Ratings = db.query(Rating).limit(5).all()

for rating in Ratings:
    print(
        f"User ID : {rating.userId}, Movie ID : {rating.movieId}, Rating : {rating.rating}, Timestamp : {rating.timestamp}")

# films with rating >= 4
high_rated_movies = db.query(Movie).join(Rating).filter(Rating.rating >= 4).limit(5).all()

for ratings in high_rated_movies:
        print(f"  Rating: {rating.rating} by user {rating.userId}")


# Get tags of films
tags = db.query(Tag).limit(5).all()

for tag in tags:
    print(f"User ID : {tag.userId}, Movie ID : {tag.movieId}, Tag : {tag.tag}, Timestamp : {tag.timestamp}")


# Test link class
links = db.query(Link).limit(5).all()

for link in links:
    print(f"Movie ID : {link.movieId}, IMDB ID : {link.imdbId}, TMDB ID : {link.tmdbId}")

# Close session
db.close()