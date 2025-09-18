# app/main.py
from fastapi import FastAPI
from app.routers import health, welcome   # import our router modules

app = FastAPI(
    title="Expense Tracker API",
    version="0.1",
    description="Day 2 - modular structure with routers and a health check."
)

# Root route (simple)


@app.get("/")
def read_root():
    """
    Root endpoint. Quick status for manual testing.
    """
    return {"message": "Hello, Expense Tracker is live!"}


# Include routers from separate modules
app.include_router(health.router)                 # adds /health
app.include_router(welcome.router, prefix="/welcome", tags=["welcome"])
