
from os import access
from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str
    
class Login(BaseModel):
    email: EmailStr
    passwd: str