#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: cleareblankline.py
@time: 2019/7/4 12:31
"""


def clearBlankLine():
    file1 = open('../infile/automatic.py', 'r', encoding='utf-8')  # 要去掉空行的文件
    file2 = open('../outfile/out.py', 'w', encoding='utf-8')  # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clearBlankLine()
