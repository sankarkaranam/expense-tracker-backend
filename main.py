from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Root route


@app.get("/")
def read_root():
    return {"message": "Hello, Expense Tracker is live!"}

# Sample route


@app.get("/welcome/{name}")
def welcome_user(name: str):
    return {"message": f"Welcome {name}, to the Expense Tracker API!"}
