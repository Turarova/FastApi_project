from fastapi import APIRouter
from typing import List
from fastapi.responses import Response

from .schemas import User, UserCreate
from .views import create_user, get_user_list, get_one_user
from .jwt import *


router = APIRouter()

@router.get("/", response_model=List[User])
async def user_list():
    return await get_user_list()


@router.post("/register", response_model=UserCreate)
async def user_register(item: UserCreate):
    return await create_user(item)


@router.post("/login")
async def user_login(item: UserCreate):
    us = await get_one_user(item)
    tokens = {"access" : create_access_token(item), "refresh" : create_refresh_token(item)}
    if verify_password(item.password, us['password']) == True:
        return tokens
    else:
        return Response(content='Data is wrong', status_code=400)
