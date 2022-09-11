from database.db import database

from .schemas import UserCreate
from .models import user
from .jwt import get_password_hash
import uuid


async def get_user_list():
    return await database.fetch_all(query=user.select())


async def create_user(item: UserCreate):   
    us = user.insert().values({"email" : item.email, "password" : get_password_hash(item.password), "activation_code" : str(uuid.uuid4())})
    exec_ = await database.execute(us) 
    return {"email" : item.email, "password" : get_password_hash(item.password)}



async def get_one_user(item):
    query = "SELECT * from account WHERE email = :email"
    res = await database.fetch_one(query=query, values={"email" : item.email})
    return dict(res)


