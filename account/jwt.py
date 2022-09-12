from datetime import datetime, timedelta
from typing import Dict, Union, Any
from jose import jwt
from passlib.context import CryptContext
from env import secret


pass_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


"""===========constants for creating access and refresh tokens============"""


ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days
ALGORITHM = "HS256"
JWT_SECRET_KEY = secret['JWT_SECRET_KEY']  # should be kept secret
JWT_REFRESH_SECRET_KEY = secret['JWT_REFRESH_SECRET_KEY'] # should be kept secret



"""=================function to hash user passwords=================="""


def verify_password(plain_password: str, hashed_password: str):
    print('VVVERRRAAA')
    res = pass_context.verify(plain_password, hashed_password)
    return res


def get_password_hash(password: str):
    return pass_context.hash(password)


"""===========functions for generating access and refresh tokens============"""


def create_access_token(subject: Union[Dict, Any]) -> str:
    to_encode = {"exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES), "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

def create_refresh_token(subject: Union[Dict, Any]) -> str:
    to_encode = {"exp": datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES), "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt