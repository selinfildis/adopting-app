from fastapi import FastAPI

from api import models
from api.database import engine
from api.routers.users import router as user_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def root():
    return {"dasd": "The orangutans are three extant species of great apes native to Indonesia and Malaysia." }


app.include_router(user_router)
