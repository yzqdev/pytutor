#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: run.py
@time: 2021/10/22 2:53
"""
import os


def main():
    os.system("uvicorn main:app --reload")


if __name__ == "__main__":
    main()


