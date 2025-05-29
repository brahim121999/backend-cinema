# 🎬 MovieLens API

Welcome to the **MovieLens API** – a RESTful API developed with **FastAPI** to explore the MovieLens database. It allows you to query information about movies, ratings, users, tags, and links to external databases (IMDB, TMDB).

---

## 🚀 Main Features

- 🔍 Search for movies by title, genre, or ID  
- ⭐ View ratings by user and by movie  
- 🏷️ Manage tags associated with movies  
- 🔗 Retrieve IMDB/TMDB IDs  
- 📊 Global database statistics  

---

## ⚙️ Prerequisites (for local development)

- Python ≥ 3.12
- An HTTP client like `httpx` or `requests`

Install `httpx`:
```bash
pip install httpx
```
---

## 🐳 Run with Docker (Recommended for Quick Testing)

1. Pull the Docker image
```
docker pull bobo7121999/img_api_film:latest
```
2. Run the container
```
docker run -d -p 5050:80 --name container_api_film bobo7121999/img_api_film:latest
```
3. Access the API
```
Swagger UI: http://localhost/docs

Health check: http://localhost/
```
---

## 📫 Essential Endpoints

| Method | URL                                    | Description                           |
|--------|----------------------------------------|------------------------------------   |
| GET    | `/`                                    | Check API status                      |
| GET    | `/movies`                              | Paginated list of movies with filters |
| GET    | `/movies/{movie_id}`                   | Movie details                         |
| GET    | `/ratings`                             | Paginated list of ratings             |
| GET    | `/ratings/{user_id}/{movie_id}`        | A user's rating for a movie           |
| GET    | `/tags`                                | List of tags                          |
| GET    | `/tags/{user_id}/{movie_id}/{tag}`     | Tag details                           |
| GET    | `/links`                               | List of IMDB/TMDB identifiers         |
| GET    | `/links/{movie_id}`                    | Identifiers for a given movie         |
| GET    | `/analytics`                           | Database statistics                   |



---

## 🧪 Example Usage with httpx

```python
import httpx

# List of movies
response = httpx.get("http://localhost/movies", params={"limit": 5})
print(response.json())

# Specific movie
response = httpx.get("http://localhost/movies/1")
print(response.json())

# Ratings
response = httpx.get("http://localhost/ratings", params={"movie_id": 1})
print(response.json())

# Tag
response = httpx.get("http://localhost/tags/5/1/superbe")
print(response.json())

# Global stats
response = httpx.get("http://localhost/analytics")
print(response.json())

```
---

## 📚 Resources

- **Swagger UI (Docs):** [http://localhost/docs](http://localhost/docs)
- **Dataset:** [MovieLens](https://grouplens.org/datasets/movielens/)

---

## Software Development Kit (SDK)

https://pypi.org/project/filmsdk-ibrahim/0.0.2/ 

---

## Public URL

*Soon*

## ✍️ Author

**Ibrahim Braham**

---
