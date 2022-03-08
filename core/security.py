from datetime import datetime, timedelta
from fastapi.security import HTTPBearer
from passlib.context import CryptContext
from jose import jwt
from core.config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM

passwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_passwd(passwd: str) -> str:
    return passwd_context.hash(passwd)

def verify_passwd(passwd: str, hash_passwd: str) -> bool:
    return passwd_context.verify(passwd, hash_passwd)

def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
def decode_access_token(token : str):
    try: 
        encoded_jwt = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except jwt.JWSError:
        return None
    return encoded_jwt

# class JWTBearer(HTTPBearer):
#     def __init__(self, auto_error: bool = True)
#         super(JWTBearer, self).__init__(auto_error=auto_error)