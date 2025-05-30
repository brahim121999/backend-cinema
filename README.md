# backend-cinema: MovieLens REST API and Python SDK

## Overview

**backend-cinema** is a RESTful API built with FastAPI that provides structured access to the [MovieLens dataset](https://grouplens.org/datasets/movielens/), a widely used benchmark dataset published by [GroupLens](https://grouplens.org/). This project enables rich queries and data exploration around movies, ratings, tags, users and external identifiers (IMDB, TMDB).

In addition to the API, the project includes a Python package — **[filmsdk_ibrahim](https://pypi.org/project/filmsdk-ibrahim/0.0.4/)** — available on PyPI. This SDK makes it easy for data analysts and scientists to interact with the MovieLens API directly from Python, supporting various data formats such as dictionaries and Pandas DataFrames.

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

### filmsdk_ibrahim Python Package

- Python SDK for accessing the MovieLens REST API  
- Available on PyPI: [filmsdk-ibrahim](https://pypi.org/project/filmsdk-ibrahim/)  
- Supports multiple output formats: Pydantic models, dictionaries, Pandas DataFrames  
- Designed for data analysis and scientific workflows  
- Easily configurable for local or remote API endpoints  

---

## Dataset Source

The dataset used in this project is the [MovieLens dataset](https://grouplens.org/datasets/movielens/) made available by [GroupLens](https://grouplens.org/). It provides real-world movie rating data commonly used in recommendation system research and development.
