from fastapi import APIRouter

# from news.func import router
from account.funcs import router as acrouter

routers = APIRouter()

# routers.include_router(router, prefix="/news")
routers.include_router(acrouter, prefix="/account")

