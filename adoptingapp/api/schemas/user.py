from datetime import datetime, date
from pydantic import BaseModel, ValidationError, validator, EmailStr


class BaseUser(BaseModel):
    full_name: str
    created_at: datetime
    date_of_birth: date
    phone_number: str
    email_address: EmailStr

    # address_id: int [ref: - address.id]
    # form_id int [ref: < form.id]
    # work_info_id int [ref: - work.id]

    class Config:
        orm_mode = True

    @validator('full_name', pre=True)
    def validate_full_name(cls, v):
        if not isinstance(v, str) or v.split() > 1:
            raise ValueError('Given fullname is not valid')
        return v


class User(BaseUser):
    id: int
    created_at: datetime
