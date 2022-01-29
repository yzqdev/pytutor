#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: main.py
@time: 2021/10/22 2:47
"""
import os
from typing import Optional

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    filename="d:/images/a.txt"
    with open(filename, 'wb') as f:
        f.write(contents)
    print(os.stat(filename))
    return {"filename": file.filename}


@app.post("/items/")
async def create_item(item: Item):
    print(type(item))
    return item


@app.get("/")
async def index():
    return 'index'
