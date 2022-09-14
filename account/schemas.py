from pydantic import BaseModel, Field, EmailStr
# from typing import Union, List

class User(BaseModel):
    email: EmailStr


class UserCreate(User):
    password: str = Field(min_length=6)

    class Config:
        orm_mode = True

class BaseUser(BaseModel):
    id: int
    email: EmailStr