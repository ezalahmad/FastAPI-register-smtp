#! /usr/bin/env python3
# models.py

from sqlalchemy import Column, String, Integer, Boolean, Enum
from schema import Roles
from connection import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=False)
    role = Column(Enum(Roles), default="user")



