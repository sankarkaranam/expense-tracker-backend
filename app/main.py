# app/main.py
from fastapi import FastAPI
from app.routers import health, welcome, user, expense
from app.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Tracker API",
    version="0.3",
    description="Day 4 - CRUD with Users & Expenses"
)

app.include_router(health.router)
app.include_router(welcome.router, prefix="/welcome", tags=["welcome"])
app.include_router(user.router)
app.include_router(expense.router)
