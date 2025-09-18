# app/db.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Database URL (SQLite for local dev)
SQLALCHEMY_DATABASE_URL = "sqlite:///./expense_tracker.db"

# Create engine (connection to DB)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal = each request will use this to talk to DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all models
Base = declarative_base()
