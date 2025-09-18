# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

# ----- USER SCHEMAS -----


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    pass  # same fields for now


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True  # important to convert SQLAlchemy objects to JSON

# ----- EXPENSE SCHEMAS -----


class ExpenseBase(BaseModel):
    title: str
    amount: float


class ExpenseCreate(ExpenseBase):
    owner_id: int


class ExpenseResponse(ExpenseBase):
    id: int
    timestamp: datetime
    owner_id: int

    class Config:
        orm_mode = True
