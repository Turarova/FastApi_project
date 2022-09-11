from pydantic import BaseModel, Field
# from typing import Union, List

class User(BaseModel):
    # id: int
    email: str


class UserCreate(User):
    password: str = Field(min_length=6)

    class Config:
        orm_mode = True

