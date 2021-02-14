
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from pydantic import ValidationError
from ..database import get_db
from ..models.user import User
from ..schemas import user as schemas

from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.post("/users/")
def create_user(user: schemas.BaseUser, db: Session = Depends(get_db)):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user


@router.put("/users/{user_id}")
def edit_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    db.query(User).filter(User.id == user_id).update(**user.dict())
    db.commit()
    user = db.query(User).get(User.id == user_id)
    return user