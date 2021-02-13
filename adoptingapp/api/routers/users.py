
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from ..database import get_db
from ..models import user as models
from ..schemas import user as schemas

from fastapi import APIRouter

router = APIRouter()


@router.get("/users/", response_model=List[schemas.User])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.post("/users/")
def create_user(user: schemas.BaseUser, db: Session = Depends(get_db)):
    db_user = models.User(full_name=user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user

@router.put("/users/{user_id}")
def edit_user(user_id:int, user: schemas.BaseUser, db: Session = Depends(get_db)):
    db_user = models.User(full_name=user.full_name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return user