from database.db import database
from .schemas import UserCreate
from .models import user
from .jwt import get_password_hash
from .send_mail import send_email

import string
import random


# async def create_superuser():
#     print(1)
#     # if item.email == "admin@admin.com":
#     query = ('GRANT ALL PRIVILEGES ON DATABASE news_db to "admin@admin.com"')
#     print(2)
#     exec_ = await database.execute(query=query)
#     print("QQUUUUEEEENNNNNN")
#     return exec_


def email_confirm(create_user):
    async def wrapped(item):
        await create_user(item)
        user_in_db = await get_one_user(item)
        if item.email != "admin@admin.com":
            await send_email(item.email, user_in_db['activation_code'])
        # return {"email" : item.email, "password" : get_password_hash(item.password)}
        return "User created"
    return wrapped



async def get_user_list():
    return await database.fetch_all(query=user.select())


@email_confirm
# @create_superuser
async def create_user(item: UserCreate):   
    us = user.insert().values({"email" : item.email, "password" : get_password_hash(item.password), "activation_code" : ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))})
    exec_ = await database.execute(us)


# async def create_superuser(item: UserCreate):   
#     us = user.insert().values({"email" : item.email, "password" : get_password_hash(item.password), "is_superuser" : True, "is_active" : True})
#     exec_ = await database.execute(us) 
#     user_in_db = await get_one_user(item)
#     await send_email(item.email, user_in_db['activation_code'])
#     return {"email" : item.email, "password" : get_password_hash(item.password)}


async def get_one_user(item):
    try:
        query = "SELECT * from account WHERE email = :email"
        res = await database.fetch_one(query=query, values={"email" : item.email})
    except ValueError: "No such user"
    else: return dict(res)
    


async def delete_user(id):
    query = "DELETE FROM account WHERE id = :id;"
    exec_ = await database.execute(query=query, values={"id" : id})
    return "User deleted"


async def get_user_by_code(code):
    try:
        query = "SELECT * from account WHERE activation_code = :activation_code"
        res = await database.fetch_one(query=query, values={"activation_code" : code})
    except ValueError: "No such user"
    else: return dict(res)


async def activate_func(code):
    query = f"UPDATE account SET is_active = true, activation_code = null WHERE activation_code = :activation_code;"
    exec_ = await database.execute(query=query, values={"activation_code" : code})
    return "User activated"

