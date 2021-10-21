#!/usr/bin/python
# -*-coding:utf-8-*-

from urllib.request import Request, urlopen
from urllib.error import URLError

someurl = "https://www.baidu.co"
req = Request(someurl)

if __name__ == '__main__':
    try:
        response = urlopen(req)

    except URLError as e:
        if hasattr(e, 'reason'):
            print('We failed to reach a server.')
            print('Reason: ', e.reason)
        elif hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code: ', e.code)

# everything is fine
