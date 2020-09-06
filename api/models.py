import datetime
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import Date, DateTime
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, unique=True)
    created_at: Column(DateTime, default=datetime.datetime.utcnow)
    date_of_birth: Column(DateTime)
    phone_number: Column(String)
    email_address: Column(String)

