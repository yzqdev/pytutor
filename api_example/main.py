#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: main.py
@time: 2021/10/22 2:47
"""
from fastapi import FastAPI, UploadFile, File

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.get("/")
async def index():
    return 'index'


def main():
    pass


if __name__ == "__main__":
    main()
