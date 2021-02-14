from datetime import date
from pydantic import BaseModel, ValidationError, validator, EmailStr
from typing import Optional


class BaseAddress(BaseModel):
    pass


class BaseWork(BaseModel):
    pass


class BaseForm(BaseModel):
    pass


class BaseUser(BaseModel):
    full_name: str
    date_of_birth: date
    phone_number: str
    email_address: EmailStr

    class Config:
        orm_mode = True

    @validator('full_name', pre=True)
    def validate_full_name(cls, v):
        if not isinstance(v, str) or len(v.split()) < 1:
            raise ValidationError('Given fullname is not valid')
        return v


class UserUpdate(BaseModel):
    phone_number: Optional[str]
    email_address: Optional[EmailStr]


class User(BaseUser):
    id: int
    # created_at: datetime

