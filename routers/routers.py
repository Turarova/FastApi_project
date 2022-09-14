from fastapi import APIRouter

from news.funcs import router, comment_router
from account.funcs import router as acrouter

routers = APIRouter()

routers.include_router(acrouter, prefix="/account")
routers.include_router(router, prefix="/articles")
routers.include_router(comment_router, prefix="/comments")



