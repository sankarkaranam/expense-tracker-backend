# app/main.py
from fastapi import FastAPI
from app.routers import health, welcome
from app.db import Base, engine

# Create all tables (if not exists)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Tracker API",
    version="0.2",
    description="Day 3 - Database setup with SQLAlchemy ORM"
)


@app.get("/")
def read_root():
    return {"message": "Expense Tracker with DB is live!"}


app.include_router(health.router)
app.include_router(welcome.router, prefix="/welcome", tags=["welcome"])
