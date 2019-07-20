#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: class1.py
@time: 2019/7/20 21:02
"""


def testFun():
    temp = [lambda x: i * x for i in range(4)]
    return temp


def main():
    print(testFun())
    for everyLambda in testFun():
        print(everyLambda(2))


if __name__ == "__main__":
    main()
