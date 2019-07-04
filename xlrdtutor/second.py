#!/usr/bin/python
# -*-coding:utf-8-*-

"""
@author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: second.py
@time: 2019/7/3 13:36
"""
import csv


def writecsv(path, data):
    with open(path, "w") as f:
        writer = csv.writer(f)
        for rowData in data:
            print("rowData=", rowData)
            writer.writerow(rowData)


def readcev(path):
    infolist = []
    with open(path, "r") as f:
        allFile = csv.reader(f)
        for row in allFile:
            infolist.append(row)
    return infolist


if __name__ == "__main__":
    path = r"../dist/1.csv"
    writecsv(path, [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(readcev(path))
