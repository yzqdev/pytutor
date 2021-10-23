#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: main.py
@time: 2021/10/22 17:05
"""
import os
import sys


def main():
    filename = 'd:/images/a.txt'
    print(os.path.getsize(filename))
    print(os.stat(filename))
    print(sys.version)
    pass


if __name__ == "__main__":
    main()
