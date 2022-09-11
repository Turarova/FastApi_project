from datetime import datetime
from pydantic import BaseModel
from typing import Union

class Article(BaseModel):
    title: str
    text: str
    image: Union[str, None] = None


class Comment(BaseModel):
    text: str
    created_at: datetime
