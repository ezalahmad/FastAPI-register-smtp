#! /usr/bin/env python3
# scurity.py

from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, Request
from jose import JWTError, jwt
# pip install python-jose | https://github.com/mpdavis/python-jose

from models import UserModel

JWT_SECRET = "secret"
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3000

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/signin")
COOKIE_NAME = "Authorization"

# create Token
def create_access_token(user):
    try:
        payload = {
                "username": user.username,
                "email": user.email,
                "role": user.role.value,
                "active": user.is_active,
                }
        return jwt.encode(payload, key=JWT_SECRET, algorithm=JWT_ALGORITHM)
    except Exception as ex:
        print(str(ex))
        raise ex

# create verify Token
def verify_token(token):
    try:
        payload = jwt.decode(token, key=JWT_SECRET)
        return payload
    except Exception as ex:
        print(str(ex))
        raise ex

# password hash
def get_password_hash(password):
    return pwd_context.hash(password)

# password verify
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_current_user_from_token(token:str=Depends(oauth2_scheme)):
    user = verify_token(token)
    return user

def get_current_user_from_cookie(request: Request) -> UserModel:
    token = request.cookies.get(COOKIE_NAME)
    if token:
        user = verify_token(token)
        return user
