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

To run the code, you can use the following command

> $ fastapi dev main.py
> $ uvicorn app.main:app --reload --port 8080

When installing `pip install pydantic[email]`. Hurmmm, it seems it does include the `email-validator` package.


```
pythonhat:~/Documents/dot-folder/code/python/FastAPI/cairocoders-register-login-fastapi$ pip install pydantic[email]
Requirement already satisfied: pydantic[email] in ./venv/lib/python3.11/site-packages (2.9.2)
Requirement already satisfied: annotated-types>=0.6.0 in ./venv/lib/python3.11/site-packages (from pydantic[email]) (0.7.0)
Requirement already satisfied: pydantic-core)]))]] =2.23.4 in ./venv/lib/python3.11/site-packages (from pydantic[email]) (2.23.4)
Requirement already satisfied: typing-extensions>=4.6.1 in ./venv/lib/python3.11/site-packages (from pydantic[email]) (4.12.2)
Requirement already satisfied: email-validator>=2.0.0 in ./venv/lib/python3.11/site-packages (from pydantic[email]) (2.2.0)
Requirement already satisfied: dnspython>=2.0.0 in ./venv/lib/python3.11/site-packages (from email-validator>=2.0.0->pydantic[email]) (2.7.0)
```

Here is another error:


```
pythonhat:~/Documents/dot-folder/code/python/FastAPI/cairocoders-register-login-fastapi$ fastapi dev main.py
INFO     Using path main.py
INFO     Resolved absolute path
/home/el/Documents/dot-folder/code/python/FastAPI/cairocoders-register-
login-fastapi/main.py
INFO     Searching for package file structure from directories with __init__.py
files
INFO     Importing from
/home/el/Documents/dot-folder/code/python/FastAPI/cairocoders-register-
login-fastapi

╭─ Python module file ─╮
│                      │
│  🐍 main.py          │
│                      │
╰──────────────────────╯

INFO     Importing module main
╭───────────────────── Traceback (most recent call last) ──────────────────────╮
│ /home/el/Documents/dot-folder/code/python/FastAPI/cairocoders-register-login │
│ -fastapi/venv/lib/python3.11/site-packages/fastapi_cli/cli.py:174 in dev     │
│                                                                              │
│   171 │                                                                      │
│   172 │   Otherwise, it uses the first [bold]FastAPI[/bold] app found in the │
│   173 │   ""                                                                │
│ ❱ 174 │   _run(                                                              │
        │   175 │   │   path=path,                                                     │
        │   176 │   │   host=host,                                                     │
        │   177 │   │   port=port,                                                     │
        │                                                                              │
        │ ╭─────────────── locals ───────────────╮                                     │
        │ │           app = None                 │                                     │
        │ │          host = '127.0.0.1'          │                                     │
        │ │          path = PosixPath('main.py') │                                     │
        │ │          port = 8000                 │                                     │
        │ │ proxy_headers = True                 │                                     │
        │ │        reload = True                 │                                     │
        │ │     root_path = '                   │                                     │
        │ ╰──────────────────────────────────────╯                                     │
        │                                                                              │
        │ /home/el/Documents/dot-folder/code/python/FastAPI/cairocoders-register-login │
        │ -fastapi/venv/lib/python3.11/site-packages/fastapi_cli/cli.py:65 in _run     │
        │                                                                              │
        │    62 │   proxy_headers: bool = False,                                       │
        │    63 ) -> None:                                                             │
│    64 │   try:                                                               │
│ ❱  65 │   │   use_uvicorn_app = get_import_string(path=path, app_name=app)   │
│    66 │   except FastAPICLIException as e:                                   │
│    67 │   │   logger.error(str(e))                                           │
│    68 │   │   raise typer.Exit(code=1) from None                             │
│                                                                              │
│ ╭─────────────── locals ───────────────╮                                     │
│ │           app = None                 │                                     │
│ │       command = 'dev'                │                                     │
│ │          host = '127.0.0.1'          │                                     │
│ │          path = PosixPath('main.py') │                                     │
│ │          port = 8000                 │                                     │
│ │ proxy_headers = True                 │                                     │
│ │        reload = True                 │                                     │
│ │     root_path = '                   │                                     │
│ │       workers = None                 │                                     │
│ ╰──────────────────────────────────────╯                                     │
│                                                                              │
│ /home/el/Documents/dot-folder/code/python/FastAPI/cairocoders-register-login │
│ -fastapi/venv/lib/python3.11/site-packages/fastapi_cli/discover.py:150 in    │
│ get_import_string                                                            │
│                                                                              │
│   147 │   │   raise FastAPICLIException(f"Path does not exist {path}")       │
│   148 │   mod_data = get_module_data_from_path(path)                         │
│   149 │   sys.path.insert(0, str(mod_data.extra_sys_path))                   │
│ ❱ 150 │   use_app_name = get_app_name(mod_data=mod_data, app_name=app_name)  │
│   151 │   import_example = Syntax(                                           │
        │   152 │   │   f"from {mod_data.module_import_str} import {use_app_name}", "p │
        │   153 │   )                                                                  │
│                                                                              │
│ ╭───────────────────────────────── locals ─────────────────────────────────╮ │
│ │ app_name = None                                                          │ │
│ │ mod_data = ModuleData(                                                   │ │
        │ │            │   module_import_str='main',                                 │ │
        │ │            │                                                             │ │
        │ │            extra_sys_path=PosixPath('/home/el/Documents/dot-folder/code… │ │
            │ │            )                                                             │ │
        │ │     path = PosixPath('main.py')                                          │ │
        │ ╰──────────────────────────────────────────────────────────────────────────╯ │
        │                                                                              │
        │ /home/el/Documents/dot-folder/code/python/FastAPI/cairocoders-register-login │
        │ -fastapi/venv/lib/python3.11/site-packages/fastapi_cli/discover.py:103 in    │
        │ get_app_name                                                                 │
        │                                                                              │
        │   100                                                                        │
        │   101 def get_app_name(*, mod_data: ModuleData, app_name: Union[str, None] = │
            │   102 │   try:                                                               │
            │ ❱ 103 │   │   mod = importlib.import_module(mod_data.module_import_str)      │
            │   104 │   except (ImportError, ValueError) as e:                             │
            │   105 │   │   logger.error(f"Import error: {e}")                             │
            │   106 │   │   logger.warning(                                                │
                │                                                                              │
                │ ╭───────────────────────────────── locals ─────────────────────────────────╮ │
                │ │ app_name = None                                                          │ │
                │ │ mod_data = ModuleData(                                                   │ │
                    │ │            │   module_import_str='main',                                 │ │
                    │ │            │                                                             │ │
                    │ │            extra_sys_path=PosixPath('/home/el/Documents/dot-folder/code… │ │
                        │ │            )                                                             │ │
                    │ ╰──────────────────────────────────────────────────────────────────────────╯ │
                    │                                                                              │
                    │ /usr/lib/python3.11/importlib/__init__.py:126 in import_module               │
                    │                                                                              │
                    │   123 │   │   │   if character != '.':                                       │
                    │   124 │   │   │   │   break                                                  │
                    │   125 │   │   │   level += 1                                                 │
                    │ ❱ 126 │   return _bootstrap._gcd_import(name[level:], package, level)        │
                    │   127                                                                        │
                    │   128                                                                        │
                    │   129 _RELOADING = {}                                                        │
                    │                                                                              │
                    │ ╭───── locals ─────╮                                                         │
                    │ │   level = 0      │                                                         │
                    │ │    name = 'main' │                                                         │
                    │ │ package = None   │                                                         │
                │ ╰──────────────────╯                                                         │
                │ in _gcd_import:1206                                                          │
                │ ╭───── locals ─────╮                                                         │
                │ │   level = 0      │                                                         │
                │ │    name = 'main' │                                                         │
                │ │ package = None   │                                                         │
                │ ╰──────────────────╯                                                         │
                │ in _find_and_load:1178                                                       │
                │ ╭────────────────── locals ──────────────────╮                               │
                │ │ module = <object object at 0x7f97fce40050> │                               │
                │ │   name = 'main'                            │                               │
                │ ╰────────────────────────────────────────────╯                               │
                │ in _find_and_load_unlocked:1149                                              │
                │ ╭───────────────────────────────── locals ─────────────────────────────────╮ │
                │ │        name = 'main'                                                     │ │
                │ │      parent = '                                                         │ │
                │ │ parent_spec = None                                                       │ │
                │ │        path = None                                                       │ │
                │ │        spec = ModuleSpec(name='main',                                    │ │
                        │ │               loader=<_frozen_importlib_external.SourceFileLoader object │ │
                        │ │               at 0x7f97fa74fd90>,                                        │ │
                        │ │               origin='/home/el/Documents/dot-folder/code/python/FastAPI… │ │
                        │ ╰──────────────────────────────────────────────────────────────────────────╯ │
                        │ in _load_unlocked:690                                                        │
                        │ ╭───────────────────────────────── locals ─────────────────────────────────╮ │
                        │ │ module = <module 'main' from                                             │ │
                        │ │          '/home/el/Documents/dot-folder/code/python/FastAPI/cairocoders… │ │
                        │ │   spec = ModuleSpec(name='main',                                         │ │
                            │ │          loader=<_frozen_importlib_external.SourceFileLoader object at   │ │
                            │ │          0x7f97fa74fd90>,                                                │ │
                            │ │          origin='/home/el/Documents/dot-folder/code/python/FastAPI/cair… │ │
                            │ ╰──────────────────────────────────────────────────────────────────────────╯ │
                            │ in exec_module:940                                                           │
                            │ ╭───────────────────────────────── locals ─────────────────────────────────╮ │
                            │ │   code = <code object <module> at 0x2d4d700, file                        │ │
                            │ │          "/home/el/Documents/dot-folder/code/python/FastAPI/cairocoders… │ │
                            │ │          line 1>                                                         │ │
                            │ │ module = <module 'main' from                                             │ │
                            │ │          '/home/el/Documents/dot-folder/code/python/FastAPI/cairocoders… │ │
                            │ │   self = <_frozen_importlib_external.SourceFileLoader object at          │ │
                            │ │          0x7f97fa74fd90>                                                 │ │
                            │ ╰──────────────────────────────────────────────────────────────────────────╯ │
                            │ in _call_with_frames_removed:241                                             │
                            │ ╭───────────────────────────────── locals ─────────────────────────────────╮ │
                            │ │ args = (                                                                 │ │
                                │ │        │   <code object <module> at 0x2d4d700, file                      │ │
                                │ │        "/home/el/Documents/dot-folder/code/python/FastAPI/cairocoders-r… │ │
                                │ │        line 1>,                                                          │ │
                                │ │        │   {                                                             │ │
                                │ │        │   │   '__name__': 'main',                                       │ │
                                │ │        │   │   '__doc__': None,                                          │ │
                                │ │        │   │   '__package__': ',                                        │ │
                                │ │        │   │   '__loader__':                                             │ │
                                │ │        <_frozen_importlib_external.SourceFileLoader object at            │ │
                                │ │        0x7f97fa74fd90>,                                                  │ │
                                │ │        │   │   '__spec__': ModuleSpec(name='main',                       │ │
                                        │ │        loader=<_frozen_importlib_external.SourceFileLoader object at     │ │
                                        │ │        0x7f97fa74fd90>,                                                  │ │
                                        │ │        origin='/home/el/Documents/dot-folder/code/python/FastAPI/cairoc… │ │
                                        │ │        │   │   '__file__':                                               │ │
                                        │ │        '/home/el/Documents/dot-folder/code/python/FastAPI/cairocoders-r… │ │
                                        │ │        │   │   '__cached__':                                             │ │
                                        │ │        '/home/el/Documents/dot-folder/code/python/FastAPI/cairocoders-r… │ │
                                        │ │        │   │   '__builtins__': {                                         │ │
                                        │ │        │   │   │   '__name__': 'builtins',                               │ │
                                        │ │        │   │   │   '__doc__': 'Built-in functions, exceptions, and other │ │
                                        │ │        objects.\n\nNoteworthy: None is the `nil'+46,                     │ │
                                        │ │        │   │   │   '__package__': ',                                    │ │
                                        │ │        │   │   │   '__loader__': <class                                  │ │
                                        │ │        '_frozen_importlib.BuiltinImporter'>,                             │ │
                                        │ │        │   │   │   '__spec__': ModuleSpec(name='builtins', loader=<class │ │
                                                │ │        '_frozen_importlib.BuiltinImporter'>, origin='built-in'),         │ │
                                        │ │        │   │   │   '__build_class__': <built-in function                 │ │
                                        │ │        __build_class__>,                                                 │ │
                                        │ │        │   │   │   '__import__': <built-in function __import__>,         │ │
                                        │ │        │   │   │   'abs': <built-in function abs>,                       │ │
                                        │ │        │   │   │   'all': <built-in function all>,                       │ │
                                        │ │        │   │   │   'any': <built-in function any>,                       │ │
                                        │ │        │   │   │   ... +147                                              │ │
                                        │ │        │   │   },                                                        │ │
                                        │ │        │   │   'Union': typing.Union,                                    │ │
                                        │ │        │   │   'FastAPI': <class 'fastapi.applications.FastAPI'>,        │ │
                                        │ │        │   │   ... +7                                                    │ │
                                        │ │        │   }                                                             │ │
                                        │ │        )                                                                 │ │
                                        │ │    f = <built-in function exec>                                          │ │
                                        │ │ kwds = {}                                                                │ │
                                        │ ╰──────────────────────────────────────────────────────────────────────────╯ │
                                        │                                                                              │
                                        │ /home/el/Documents/dot-folder/code/python/FastAPI/cairocoders-register-login │
                                        │ -fastapi/main.py:14 in <module>                                              │
                                        │                                                                              │
                                        │   11 # import os                                                             │
                                        │   12                                                                         │
                                        │   13 # Model                                                                 │
                                        2     role = Column(Enum(Roles), default="user")¬                                                                                                                                             3 ¬                                                                                                                                                                                           4 ¬                                                                                                                                                                                         ~                                                                                                                                                                                             ~                                                                                                                                                                                             ~                                                                                                                                                                                             ~                                                                                                                                                                                             ~                                                                                                                                                                                             ~                                                                                                                                                                                             ~                                                                                                                                                                                             ~                                                                                                                                                                                             ~                                                                                                                                                     │ ❱ 14 from models import UserModel                                            │
                                        │   15                                                                         │
                                        │   16 templates = Jinja2Templates(directory="templates")                      │
                                        │   17                                                                         │
                                        │                                                                              │
                                        │ ╭────────────────── locals ───────────────────╮                              │
                                        │ │ engine = Engine(sqlite:///fastapi_users.db) │                              │
                                        │ │  Union = typing.Union                       │                              │
                                        │ ╰─────────────────────────────────────────────╯                              │
                                        ╰──────────────────────────────────────────────────────────────────────────────╯
                                        ╭──────────────────────────────────────────────────────────────────────────────╮
                                        │  /home/el/Documents/dot-folder/code/python/FastAPI/cairocoders-register-logi │
                                        │ n-fastapi/models.py:13                                                       │
                                        │     is_active = Column(Boolean, default=True                                 │
                                                │                       ▲                                                      │
                                                ╰──────────────────────────────────────────────────────────────────────────────╯
                                                SyntaxError: '(' was never closed

```
