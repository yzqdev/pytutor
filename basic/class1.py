#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: class1.py
@time: 2019/7/1 12:02
"""


def slicet():
    name = 'My name is Mike'
    print(name[0])
    'M'
    print(name[-4])
    'M'
    print(name[11:14])  # from 11th to 14th, 14th one is excluded
    'Mik'
    print(name[11:15])  # from 11th to 15th, 15th one is excluded
    'Mike'
    print(name[5:])
    'me is Mike'
    print(name[:5])
    for i in range(1, 10):
        for j in range(1, 10):
            print('{} X {} = {}'.format(i, j, i * j))


def writeFile(name, msg):
    desktop_path = '/Users/Hou/Desktop/'
    full_path = desktop_path + name + '.txt'
    file = open(full_path, 'w')
    file.write(msg)
    file.close()
    print('Done')


def listoperate():
    a = []
    for i in range(1, 11):
        a.append(i)
    # 等同于
    b = [i for i in range(1, 11)]
    a = [i ** 2 for i in range(1, 10)]
    c = [j + 1 for j in range(1, 10)]
    k = [n for n in range(1, 10) if n % 2 == 0]
    z = [letter.lower() for letter in 'ABCDEFGHIGKLMN']
    # 字典推导式
    d = {i: i + 1 for i in range(4)}
    g = {i: j for i, j in zip(range(1, 6), 'abcde')}
    g = {i: j.upper() for i, j in zip(range(1, 6), 'abcde')}
    print(z)


def dicop():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    for num, letter in enumerate(letters):
        print(letter, 'is', num + 1)


if __name__ == "__main__":
    # slicet()
    # writeFile()
    listoperate()
    dicop()
