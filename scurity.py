#! /usr/bin/env python3
# scurity.py

from passlib.context import CryptContext
from jose import JWTError, jwt
# pip install python-jose | https://github.com/mpdavis/python-jose

from models import UserModel

JWT_SECRET = "secret"
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 3000

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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

# password hash
def get_password_hash(password):
    return pwd_context.hash(password)

