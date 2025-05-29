# backend-cinema: MovieLens REST API and Python SDK

## Overview

**backend-cinema** is a RESTful API built with FastAPI that provides access to the MovieLens dataset, enabling rich queries and data exploration around movies, ratings, tags, users, and external identifiers (IMDB, TMDB). Alongside the API, the **filmsdk-ibrahim** Python SDK offers an easy-to-use interface for data analysts and scientists to interact with the API using native Python objects, dictionaries, or Pandas DataFrames.

---

## Features

### MovieLens API

- Search movies by title, genre, or ID
- Retrieve detailed movie information
- Query user and movie ratings with pagination
- Manage tags associated with movies
- Access IMDB and TMDB IDs for movies
- Fetch global database statistics

---

### filmsdk-ibrahim SDK

- Python client to interact with the MovieLens API seamlessly
- Supports multiple output formats: Pydantic models, dictionaries, and Pandas DataFrames
- Designed for data analysis and scientific workflows
- Simple configuration for local or remote API endpoints

---
