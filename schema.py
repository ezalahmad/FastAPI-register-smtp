#! /usr/bin/env python3
 # schema.py

from datetime import date
from enum import Enum
from pydantic import BaseModel, EmailStr # pip install pydantic[email]
from fastapi import Form

class UserSchema(BaseModel):
    email: EmailStr
    username: str
    password: str

    class Config:
        orm_mode = True


class Roles(Enum):
    user = "user"
    admin = "admin"
