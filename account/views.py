from database.db import database

from .schemas import UserCreate
from .models import user
from .jwt import get_password_hash
import uuid
from .send_mail import send_email

import string
import random


async def get_user_list():
    return await database.fetch_all(query=user.select())


async def create_user(item: UserCreate):   
    us = user.insert().values({"email" : item.email, "password" : get_password_hash(item.password), "activation_code" : ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))})
    exec_ = await database.execute(us) 
    user_in_db = await get_one_user(item)
    await send_email(item.email, user_in_db['activation_code'])
    return {"email" : item.email, "password" : get_password_hash(item.password)}



async def get_one_user(item):
    query = "SELECT * from account WHERE email = :email"
    res = await database.fetch_one(query=query, values={"email" : item.email})
    return dict(res)


