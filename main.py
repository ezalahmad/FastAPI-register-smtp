#! /usr/bin/env python3
 # main.py

from typing import Union

from fastapi import FastAPI, Request, Depends, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from connection import Base, engine, sess_db
from sqlalchemy.orm import Session

# Scurity
from scurity import get_password_hash

# Repository
from repositoryuser import UserRepository

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
def signupuser(db:Session=Depends(sess_db), username: str = Form(),
                                            email: str = Form(),
                                            password: str = Form()):
    print(username)
    print(email)
    print(password)

    userRepository = UserRepository(db)

    signup = UserModel(email=email, username=username, password=get_password_hash(password))
    success = userRepository.create_user(signup)

    if success:
        return "User created successfully."
    else:
        raise HTTPException(status_code=400, detail="Credentials not valid")

