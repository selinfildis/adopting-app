from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError

from .database import engine, Base
from .routers.users import router as user_router

Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.exception_handler(IntegrityError)
async def unicorn_exception_handler(request: Request, exc: IntegrityError):
    return JSONResponse(
        status_code=409,
        content={"message": f"you cannot create duplicate entries: {exc.orig.pgerror}"},
    )


@app.get("/")
async def root():
    return "HELLO"


app.include_router(user_router)
