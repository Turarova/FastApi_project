from fastapi import FastAPI
from routers.routers import routers
from database.db import database, Base, engine

app = FastAPI()


@app.on_event("startup")
async def startup():    
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(routers)

Base.metadata.create_all(bind=engine)

