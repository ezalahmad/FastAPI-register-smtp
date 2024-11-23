#! /usr/bin/env python3
 # main.py

from typing import Union

from fastapi import FastAPI, Request, Depends, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from connection import Base, engine, sess_db
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse

# Scurity
from scurity import get_password_hash, create_access_token, verify_token

# Repository
from repositoryuser import UserRepository, SendEmailVerify

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

@app.post("/signinuser")
def signin_user(db: Session = Depends(sess_db), username: str = Form(...), password: str = Form(...)):
    print(username)
    print(password)
    userRepository = UserRepository(db)
    db_user = userRepository.get_user_by_username(username)

    if not db_user:
        return "username or password is not valid"

    return "Success"

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

    db_user = userRepository.get_user_by_username(username)
    if db_user:
        return "username is not valid"

    signup = UserModel(email=email, username=username, password=get_password_hash(password))
    success = userRepository.create_user(signup)
    token = create_access_token(signup)

    print(token)

    SendEmailVerify.sendVerify(token)

    if success:
        return "User created successfully."
    else:
        raise HTTPException(status_code=400, detail="Credentials not valid")

@app.get("/user/verify/{token}")
def verify_user(token, db:Session=Depends(sess_db)):
    userRepository = UserRepository(db)
    payload = verify_token(token)
    username = payload.get("username")
    db_user = userRepository.get_user_by_username(username)
    # db_user = userRepository.get_user_by_username(username)

    if not username:
        raise HTTPException(status_code=401, detail="Credentials not correct")

    if db_user.is_active == True:
        return "User verified successfully."

    db_user.is_active = True
    db.commit()
    # response = RedirectResponse(url="/user/signin", status_code=status.HTTP_302_FOUND)
    response = RedirectResponse(url="/user/signin")

    return response

