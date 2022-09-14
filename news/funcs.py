from fastapi import APIRouter, Depends
from typing import List

from .schemas import *
from .views import *
from account.funcs import http_bearer

router = APIRouter()
comment_router = APIRouter()


@router.get("/", response_model=List[Article])
async def article_list():
    return await get_article_list()
    

@router.post("/create")
async def article_create(item: Article, token = Depends(http_bearer)):
    return await create_article(item)



@router.delete("/delete/{id}")
async def article_delete(id: int, token : str = Depends(http_bearer)):
    return await delete_article(id)


@router.patch("/update/{id}")
async def article_update(id: int, item : Article, token : str = Depends(http_bearer)):
    return await update_article(id, item)





@comment_router.get("/{article_id}", response_model=List[Comment])
async def comment_list(id: int, token = Depends(http_bearer)):
    return await get_comment_list(id)


@comment_router.post("/create_comment")
async def comment_create(item: Comment, token = Depends(http_bearer)):
    return await create_comment(item)


@comment_router.delete("/delete_comment/{id}")
async def comment_delete(id: int, token = Depends(http_bearer)):
    return await delete_comment(id)



