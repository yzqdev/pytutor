#!/usr/bin/python
# -*-coding:utf-8-*-
"""
@Author: YangZhengqian
@contact: xx@xx.com
@software: PyCharm
@file: class3.py
@time: 2019/7/4 14:26
"""
import requests
import json


class CocaCola:
    formula = ['caffeine', 'sugar', 'water', 'soda']

    def drink(self):
        print('Energy!')


def main():
    coke = CocaCola()
    coke.drink()

    # 执行API调用并存储响应
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    print("Status code:", r.status_code)
    # 将API响应存储在一个变量中
    response_dict = r.json()
    aa = json.dumps(response_dict, ensure_ascii=False)
    with open("1.json", 'w', encoding='utf-8') as gitapi:
        gitapi.write(aa)
    # 处理结果


def bianli():
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    for name, lang in favorite_languages.items():
        print(name.title() + lang.title())


def numJewelsInStones( J: str, S: str) -> int:

    return sum(S.count(i) for i in J)


if __name__ == "__main__":
    # bianli()
    a=numJewelsInStones('aA',"adeeaarerAAeer")
    print(a)