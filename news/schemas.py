from datetime import datetime
from pydantic import BaseModel
from typing import Union

class Article_Create(BaseModel):
    title: str
    text: str
    image: Union[str, None] = None

    class Config:
        orm_mode = True


class Article(Article_Create):
    id: int


class Comment(BaseModel):
    text: str
    article_id : int

    class Config:
        orm_mode = True