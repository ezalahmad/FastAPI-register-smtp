---
title: FastAPI Register Login SMTP Email
Author: El Ahmad
date: November 15, 2024
tags: Python, FastAPI, Register, Login, SMTP, Email
slug: fastapi-register-login-smtp-email
---

Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Code](#code)

# Introduction
<a name="introduction"></a>

In this article, we will be learning how to create a fastapi register and login app with smtp email.

This will be a step by step guide:

1. Requirements
2. Code

# Requirements
<a name="requirements"></a>

1. [FastAPI](https://fastapi.tiangolo.com/)
2. [SMTP](https://en.wikipedia.org/wiki/Simple_Mail_Transfer_Protocol)
3. [Pydantic](https://pydantic-docs.helpmanual.io/)
4. [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/)
5. [Uvicorn](https://www.uvicorn.org/)
6. [SQLAlchemy](https://www.sqlalchemy.org/)

> $ pip install "fastapi[standard]"

Once installed run the following command `pip list`

```
Package           Version
----------------- -----------
annotated-types   0.7.0
anyio             4.6.2.post1
certifi           2024.8.30
click             8.1.7
dnspython         2.7.0
email_validator   2.2.0
fastapi           0.115.5
fastapi-cli       0.0.5
h11               0.14.0
httpcore          1.0.7
httptools         0.6.4
httpx             0.27.2
idna              3.10
Jinja2            3.1.4
markdown-it-py    3.0.0
MarkupSafe        3.0.2
mdurl             0.1.2
pip               23.0.1
pydantic          2.9.2
pydantic_core     2.23.4
Pygments          2.18.0
python-dotenv     1.0.1
python-multipart  0.0.17
PyYAML            6.0.2
rich              13.9.4
setuptools        66.1.1
shellingham       1.5.4
sniffio           1.3.1
starlette         0.41.2
typer             0.13.0
typing_extensions 4.12.2
uvicorn           0.32.0
uvloop            0.21.0
watchfiles        0.24.0
websockets        14.1
```

Next, install the following packages

> $ pip install sqlalchemy

Now, we create a `main.py` file and copy the following code

```python
 # main.py

from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

```
Let's run the following command

> $ fastapi dev main.py

You can open the following link `http://localhost:8000/`

Next, we create a `pyproject.toml` file and copy the following code

```toml
[tool.poetry]
name = "fastapi-register-login-smtp-email"
version = "0.1.0"
description = ""
authors = ["El Ahmad <VYi0d@example.com>"]
readme = "README.md"
packages = [{include = "fastapi_register_login_smtp_email"}]

[tool.poetry.dependencies]
python = "^3.11"
fastapi = "^0.103.1"
uvicorn = "^0.23.2"
pydantic = "^2.3.0"
sqlalchemy = "^2.0.20"
python-dotenv = "^1.0.0"
jinja2 = "^3.1.2"
```

# Code
<a name="code"></a>

```python
import smtplib
from email.message import EmailMessage
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI()  # Create a FastAPI instance

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")  # Create Jinja2 templates instance

app.mount("/static", StaticFiles(directory="static"), name="static")  # Mount static files

class User(BaseModel):
    username: str
    email: str
    password: str

users = {}  # Dictionary to store users

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/register")
async def register(user: User):
    if user.email in users:  # Check if email already exists
        raise HTTPException(status_code=400, detail="Email already exists")
    users[user.email] = user  # Add user to dictionary
    return {"message": "User registered successfully"}  # Return success message

@app.post("/login")
async def login(user: User):
    if user.email not in users:  # Check if email exists
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if users[user.email].password != user.password:  # Check if password is correct
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}  # Return success message

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)  # Run the FastAPI application
```
