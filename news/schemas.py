from datetime import datetime
from pydantic import BaseModel
from typing import Union, List

class Article(BaseModel):
    title: str
    text: str
    image: Union[List[str], None] = None


class Comment(BaseModel):
    text: str
    created_at: datetime
