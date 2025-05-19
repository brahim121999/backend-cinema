# MovieLens API

Welcome to the **MovieLens API** - a RESTful API developed with **FastAPI** to explore the MovieLens database. It allows you to query information about movies, ratings, users, tags, and links to external databases (IMDB, TMDB).

## Main Features

- Search for movies by title, genre, or ID
- View ratings by user and by movie
- Manage tags associated with movies
- Retrieve IMDB/TMDB IDs
- Global database statistics

---

## Prerequisites

- Python ≥ 3.12
- An HTTP client like `httpx` or `requests`

Quick installation of `httpx`:

```bash
pip install httpx
```

## Getting Started with the API

The API is accessible at the following address:

The Swagger interface is available here:
```
http://localhost:8000/docs
```

## Essential Endpoints

| Method | URL                                 | Description |
|--------|--------------------------------------|-------------|
| GET    | `/`                                  | Checks API functionality |
| GET    | `/movies`                            | Paginated list of movies with filters |
| GET    | `/movies/{movie_id}`                 | Movie details |
| GET    | `/ratings`                           | Paginated list of ratings |
| GET    | `/ratings/{user_id}/{movie_id}`      | A user's rating for a movie |
| GET    | `/tags`                              | List of tags |
| GET    | `/tags/{user_id}/{movie_id}/{tag}`   | Tag details |
| GET    | `/links`                             | List of IMDB/TMDB identifiers |
| GET    | `/links/{movie_id}`                  | Identifiers for a given movie |
| GET    | `/analytics`                         | Database statistics |



---

## Example of usage with `httpx`

### List of films

```python
import httpx

response = httpx.get("http://localhost:8000/movies", params={"limit": 5})
print(response.json())
```

### Get a specific film

```python
movie_id = 1
response = httpx.get(f"http://localhost:8000/movies/{movie_id}")
print(response.json())
```

### Get ratings for a specific film

```python
response = httpx.get("http://localhost:8000/ratings", params={"movie_id": 1})
print(response.json())
```

### Get a specific tag

```python
response = httpx.get("http://localhost:8000/tags/5/1/superbe")
print(response.json())
```

### Get global statistics

```python
response = httpx.get("http://localhost:8000/analytics")
print(response.json())
```

---

## Conditions of usage

- This API is designed for educational and experimental purposes.

- Please avoid making mass requests without frequency control (rate-limiting is not implemented yet).

- You can integrate it into notebooks, applications, or data visualization projects to explore the MovieLens data.

---

---

## Ressources

- Swagger UI : [http://localhost:8000/docs](http://localhost:8000/docs)
- Technical documentation: available via Swagger
- Data set MovieLens : [https://grouplens.org/datasets/movielens/](https://grouplens.org/datasets/movielens/)

---

## Software Development Kit (SDK)

*Soon*

---

## Public URL

*Soon*

## Author

Ibrahim Braham

---
