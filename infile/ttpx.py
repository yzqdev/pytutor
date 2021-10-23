#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: ttpx.py
@time: 2021/10/22 3:21
"""
import httpx


def main():
    res=httpx.get("https://www.baidu.com")
    print(res.text)
    pass


if __name__ == "__main__":
    main()
