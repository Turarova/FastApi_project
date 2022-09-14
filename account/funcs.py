from fastapi import APIRouter, Depends
from typing import List
from fastapi.responses import Response
from fastapi.security import HTTPBearer

from .schemas import User, UserCreate, BaseUser
from .views import create_user, get_user_list, get_one_user, delete_user, activate_func
from .jwt import *

# from .permissions import IsAdmin
# from jose import JWTError

router = APIRouter()

http_bearer = HTTPBearer()


@router.get("/", response_model=List[BaseUser])
async def user_list(token : str = Depends(http_bearer)):
    return await get_user_list()
    # print("tokkeeenn", token.credentials)
    # user = decode_token(token)
    # print("UUUUUSSSSSSEEEERRRRRR", user) 
    


@router.post("/register")
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


@router.post("/activation")
async def activate(code: str, token = Depends(http_bearer)):
    return await activate_func(code)
    


@router.delete("/delete/{id}")
async def user_delete(id: int, token : str = Depends(http_bearer)):
    return await delete_user(id)


# @router.get("/user_from_req")
# async def get_current_user(token: str = Depends(http_bearer)):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
#         email: str = payload.get("subject")
#         if email is None:
#             raise credentials_exception
#     except JWTError:
#         raise credentials_exception
#     return email

# @router.post("/admin")
# async def superuser_create():
#     return await create_superuser()