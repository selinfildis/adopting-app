from fastapi import FastAPI

from .database import engine, Base
from .routers.users import router as user_router

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.get("/")
async def root():
    return {"dasd": "The orangutans are three extant species of great apes native to Indonesia and Malaysia." }


app.include_router(user_router)
