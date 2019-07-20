#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: util.py
@time: 2019/7/17 13:04
"""


class Util:
    def __init__(self):
        print("program started")
    """
    输出99乘法表
    """
    def showChengfabiao(self):

        for i in range(1, 10):
            for j in range(1, i + 1):
                print('%d*%d=%d' % (i, j, i * j), end='  ')
            print()


if __name__ == "__main__":
    pass
