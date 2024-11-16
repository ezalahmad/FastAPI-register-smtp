#! /usr/bin/env python3
 # main.py

from typing import Union
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

