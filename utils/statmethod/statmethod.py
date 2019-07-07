#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: statmethod.py
@time: 2019/7/7 1:55
"""


class Statmethod:
    def strip_control_characters(self, s):
        word = ''
        for i in s:
            if ord(i) > 31 or ord(i) == 10 or ord(i) == 13:
                word += i
        return word
