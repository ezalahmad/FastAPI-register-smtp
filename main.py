#! /usr/bin/env python3
 # main.py

from typing import Union

from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from connection import Base, engine, sess_db
from sqlalchemy.orm import Session
# import os

# Model
from models import UserModel

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# db_engine
Base.metadata.create_all(bind=engine)

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/user/signin")
def login(req: Request):
    return templates.TemplateResponse("/signin.html", {"request": req})

@app.get("/user/signup")
def signup(req: Request):
    return templates.TemplateResponse("/signup.html", {"request": req})

@app.post("/signupuser")
def signupuser(db:Session=Depends(sess_db),
               username: str = Form(),
               email: str = Form(),
               password: str = Form()):
    print(username)
    print(email)
    print(password)
    return "User created successfully."

