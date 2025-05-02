from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from typing import Optional

import models


# --- Movies ---
def get_movie(db: Session, movie_id: int):
    """Get a movie by its ID."""
    return db.query(models.Movie).filter(models.Movie.movieId == movie_id).first()


def get_movies(db: Session, skip: int = 0, limit: int = 100, title: str = None, genre: str = None):
    """Get a list of movies with optional filters."""
    query = db.query(models.Movie)

    if title:
        query = query.filter(models.Movie.title.ilike(f"%{title}%"))
    if genre:
        query = query.filter(models.Movie.genres.ilike(f"%{genre}%"))

    return query.offset(skip).limit(limit).all()


# --- Ratings ---
def get_rating(db: Session, user_id: int, movie_id: int):
    """Get a rating based on the (userId, movieId) pair."""
    return db.query(models.Rating).filter(
        models.Rating.userId == user_id,
        models.Rating.movieId == movie_id
    ).first()


def get_ratings(db: Session, skip: int = 0, limit: int = 100, movie_id: int = None, user_id: int = None,
                min_rating: float = None):
    """Get a list of ratings with optional filters."""
    query = db.query(models.Rating)

    if movie_id:
        query = query.filter(models.Rating.movieId == movie_id)
    if user_id:
        query = query.filter(models.Rating.userId == user_id)
    if min_rating:
        query = query.filter(models.Rating.rating >= min_rating)

    return query.offset(skip).limit(limit).all()


# --- Tags ---
def get_tag(db: Session, user_id: int, movie_id: int, tag_text: str):
    """Get a tag by userId, movieId and tag text."""
    return (
        db.query(models.Tag)
        .filter(
            models.Tag.userId == user_id,
            models.Tag.movieId == movie_id,
            models.Tag.tag == tag_text
        )
        .first()
    )


def get_tags(
        db: Session,
        skip: int = 0,
        limit: int = 100,
        movie_id: Optional[int] = None,
        user_id: Optional[int] = None
):
    """Get a list of tags with optional filters."""
    query = db.query(models.Tag)

    if movie_id is not None:
        query = query.filter(models.Tag.movieId == movie_id)
    if user_id is not None:
        query = query.filter(models.Tag.userId == user_id)

    return query.offset(skip).limit(limit).all()


# --- Links ---
def get_link(db: Session, movie_id: int):
    """Return the IMDB and TMDB links associated with a specific movie."""
    return db.query(models.Link).filter(models.Link.movieId == movie_id).first()


def get_links(db: Session, skip: int = 0, limit: int = 100):
    """Return a paginated list of movie IMDB and TMDB links."""
    return db.query(models.Link).offset(skip).limit(limit).all()


# --- Analytical Queries ---
def get_movie_count(db: Session):
    """Return the total number of movies."""
    return db.query(models.Movie).count()


def get_rating_count(db: Session):
    """Return the total number of ratings."""
    return db.query(models.Rating).count()


def get_tag_count(db: Session):
    """Return the total number of tags."""
    return db.query(models.Tag).count()


def get_link_count(db: Session):
    """Return the total number of links."""
    return db.query(models.Link).count()