#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: automatic.py
@time: 2019/7/3 22:50
"""


def gencustom():
    str = input("请输入名字")
    try:
        num = int(input("请输入要生成的序号数")) - 1
        frontsig = input("输入前缀")
        endsig = input("输入后缀")
        for n in range(1, num):
            front = frontsig + str + repr(n) + endsig + ","
            print(front, end='')
    except ValueError as e:
        print("亲输入数字!")


if __name__ == "__main__":
    gencustom()
