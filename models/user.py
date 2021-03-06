from datetime import datetime
from optparse import Option
from typing import Optional
from pydantic import BaseModel, EmailStr, constr, validator
import datetime


class User(BaseModel):
    id: Optional[str] = None
    name: str
    email: EmailStr
    is_company: bool
    h_passwd: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    

class UserIn(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)
    password2: str
    is_company: bool = False

    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values["password"]:
            raise ValueError("passwords don't match")
        return v

    
    