from fastapi import FastAPI, HTTPException, Query, Path, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from database import SessionLocal
import query_helpers as helpers
import schemas


app = FastAPI(
    title="Cinema API",
    description="Cinema API description",
    version="0.1"
)



# dependency for session of the db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

api_description = """
Welcome to the **MovieLens API**

This API allows you to interact with a database inspired by the popular
[MovieLens dataset](https://grouplens.org/datasets/movielens/).

It’s perfect for learning how to consume a REST API with movie-related data including users, ratings, tags, and external links (IMDB, TMDB).

### Available Features:
- Search for a movie by ID or list all movies
- View ratings by user and/or movie
- Access tags applied by users to movies
- Retrieve IMDB / TMDB links for a movie
- See overall statistics about the database

All endpoints support pagination (`skip`, `limit`) and optional filters where applicable.

### Good to Know
- You can test all endpoints directly via the Swagger UI below.
- For any error (e.g., non-existent ID), a clear response is returned with the appropriate HTTP status code.
"""

# FastAPI application initialization
app = FastAPI(
    title="MovieLens API",
    description=api_description,
    version="0.1"
)

# Endpoint to get statistics about the database
@app.get(
    "/analytics",
    summary="Get statistics",
    description="""
    Returns an analytical summary of the database:
    - Total number of movies
    - Total number of ratings
    - Total number of tags
    - Number of links to IMDB/TMDB
    """,
    response_model=schemas.AnalyticsResponse,
    tags=["analytics"]
)
def get_analytics(db: Session = Depends(get_db)):
    movie_count = helpers.get_movie_count(db)
    rating_count = helpers.get_rating_count(db)
    tag_count = helpers.get_tag_count(db)
    link_count = helpers.get_link_count(db)
    return schemas.AnalyticsResponse(
        movie_count=movie_count,
        rating_count=rating_count,
        tag_count=tag_count,
        link_count=link_count
    )


# Endpoint ot check api health
@app.get(
    "/",
    summary="test api health",
    description="to verify if api works well",
    response_description="state of the api",
    operation_id="health check",
    tags=["monitoring"]
)

async def root():
    return {"message": "api is working well"}

# Endpoint to get a film by its id
@app.get(
    "/movies/{movie_id}",
    summary="get a film by its id",
    description="get a film informations by its id",
    response_description="film informations",
    response_model=schemas.MovieDetailed,
    tags=["films"]
)

def read_movie(movie_id: int = Path(..., description="id of the film"),  db: Session = Depends(get_db)):
    movie = helpers.get_movie(db, movie_id)
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie with id {movie_id} is not found")
    return movie

# Endpoint for a list of films (with pagination and optional title, genre, skip, limit filters)
@app.get(
     "/movies",
     summary="To list films",
     description="Returns a list of films with pagination and optional filters by title or genre..",
     response_description="List of films",
     response_model=List[schemas.MovieSimple],
     tags=["films"],
    )

def list_movies(skip: int = Query(0, ge=0, description="Number of results to ignore"),limit: int = Query(100, le=1000, description="Maximum number of results to return"),title: str = Query(None, description="FIlter by title"),genre: str = Query(None, description="Filter by genre"), db: Session = Depends(get_db)):
    movies = helpers.get_movies(db, skip=skip, limit=limit, title=title, genre=genre)
    return movies

# Endpoint to obtain an evaluation by user and film
@app.get(
     "/ratings/{user_id}/{movie_id}",
     summary="get rating by user and film",
     description="Returns evaluation of the user for selected film",
     response_description="Detail of the rating",
     response_model=schemas.RatingSimple,
     tags=["evaluations"],
)

def read_rating(user_id: int = Path(..., description="ID of the user"),movie_id: int = Path(..., description="ID of the film"),db: Session = Depends(get_db)):
    rating = helpers.get_rating(db, user_id=user_id, movie_id=movie_id)
    if rating is None:
        raise HTTPException(status_code=404,detail=f"Any rating found for user {user_id} and film {movie_id}")
    return rating


# Endpoint to retrieve a list of ratings with filters
@app.get(
    "/ratings",
    summary="List ratings",
    description="Returns a list of ratings with pagination and optional filters (movie, user, minimum rating).",
    response_description="List of ratings",
    response_model=List[schemas.RatingSimple],
    tags=["ratings"],
)
def list_ratings(
    skip: int = Query(0, ge=0, description="Number of results to skip"),
    limit: int = Query(100, le=1000, description="Maximum number of results to return"),
    movie_id: Optional[int] = Query(None, description="Filter by movie ID"),
    user_id: Optional[int] = Query(None, description="Filter by user ID"),
    min_rating: Optional[float] = Query(None, ge=0.0, le=5.0, description="Filter ratings greater than or equal to this value"),
    db: Session = Depends(get_db)
):
    ratings = helpers.get_ratings(
        db,
        skip=skip,
        limit=limit,
        movie_id=movie_id,
        user_id=user_id,
        min_rating=min_rating
    )
    return ratings


# Endpoint to return a tag for a given user and movie, with the tag text
@app.get(
    "/tags/{user_id}/{movie_id}/{tag_text}",
    summary="Get a specific tag",
    description="Returns a tag for a given user and movie, with the tag text.",
    response_model=schemas.TagSimple,
    tags=["tags"],
)
def read_tag(
    user_id: int = Path(..., description="User ID"),
    movie_id: int = Path(..., description="Movie ID"),
    tag_text: str = Path(..., description="Exact content of the tag"),
    db: Session = Depends(get_db)
):
    result = helpers.get_tag(db, user_id=user_id, movie_id=movie_id, tag_text=tag_text)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"Tag not found for user {user_id}, movie {movie_id}, and tag '{tag_text}'"
        )
    return result

# Endpoint to return a list of tags with pagination and optional filters by user or movie
@app.get(
    "/tags",
    summary="List tags",
    description="Returns a list of tags with pagination and optional filters by user or movie.",
    response_model=List[schemas.TagSimple],
    tags=["tags"],
)
def list_tags(
    skip: int = Query(0, ge=0, description="Number of results to skip"),
    limit: int = Query(100, le=1000, description="Maximum number of results to return"),
    movie_id: Optional[int] = Query(None, description="Filter by movie ID"),
    user_id: Optional[int] = Query(None, description="Filter by user ID"),
    db: Session = Depends(get_db)
):
    return helpers.get_tags(db, skip=skip, limit=limit, movie_id=movie_id, user_id=user_id)

# Endpoint to return the IMDB and TMDB identifiers for a given movie
@app.get(
    "/links/{movie_id}",
    summary="Get movie link",
    description="Returns the IMDB and TMDB identifiers for a given movie.",
    response_model=schemas.LinkSimple,
    tags=["links"],
)
def read_link(
    movie_id: int = Path(..., description="Movie ID"),
    db: Session = Depends(get_db)
):
    result = helpers.get_link(db, movie_id=movie_id)
    if result is None:
        raise HTTPException(
            status_code=404,
            detail=f"No link found for the movie with ID {movie_id}"
        )
    return result

# Endpoint to return a paginated list of IMDB and TMDB identifiers for all movies
@app.get(
    "/links",
    summary="List movie links",
    description="Returns a paginated list of IMDB and TMDB identifiers for all movies.",
    response_model=List[schemas.LinkSimple],
    tags=["links"],
)
def list_links(
    skip: int = Query(0, ge=0, description="Number of results to skip"),
    limit: int = Query(100, le=1000, description="Maximum number of results to return"),
    db: Session = Depends(get_db)
):
    return helpers.get_links(db, skip=skip, limit=limit)

# Endpoint to get statistics about the database
@app.get(
    "/analytics",
    summary="Get analytics statistics",
    description="Returns the total number of movies, ratings, tags, and links.",
    response_model=schemas.AnalyticsResponse,
    tags=["analytics"]
)
def get_analytics(db: Session = Depends(get_db)):
    movie_count = helpers.get_movie_count(db)
    rating_count = helpers.get_rating_count(db)
    tag_count = helpers.get_tag_count(db)
    link_count = helpers.get_link_count(db)
    return schemas.AnalyticsResponse(
        movie_count=movie_count,
        rating_count=rating_count,
        tag_count=tag_count,
        link_count=link_count
    )

