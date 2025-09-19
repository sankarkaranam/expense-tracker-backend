# app/main.py
from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import health, welcome, user, expense

# Create DB tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API")

app.include_router(health.router)
app.include_router(welcome.router)
app.include_router(user.router)
app.include_router(expense.router)
