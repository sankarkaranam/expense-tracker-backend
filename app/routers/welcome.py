# app/routers/welcome.py
from fastapi import APIRouter

router = APIRouter()


@router.get("/{name}", summary="Welcome user by name")
def greet(name: str):
    """
    Example route to demonstrate path parameter handling.
    GET /welcome/Sankar -> {"message": "Welcome Sankar, to the Expense Tracker API!"}
    """
    return {"message": f"Welcome {name}, to the Expense Tracker API!"}
