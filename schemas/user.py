from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    email: EmailStr
    name: str
    user_type: str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None

class UserInDB(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True

class User(UserInDB):
    pass