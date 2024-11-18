#! /usr/bin/env python3
# scurity.py

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# password hash
def get_password_hash(password):
    return pwd_context.hash(password)

