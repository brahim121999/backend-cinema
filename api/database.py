"""Database configuration"""
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./movies.db"

# Create a database engine that establishes connection with our SQLite database (movies.db)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Define SessionLocal which will be used to create database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define Base which will serve as the base class for our SQLAlchemy models
Base = declarative_base()

# To test the connection to the db
if __name__ == "__main__":
     try:
         with engine.connect() as conn:
             print("Database connection successful")
     except Exception as e:
         print(f"Database connection error: {e}")