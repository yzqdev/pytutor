from urllib.request import Request, urlopen
from urllib.error import URLError
someurl="https://www.baidu.com"
req = Request(someurl)

try:
    response = urlopen(req)
except URLError as e:
    if hasattr(e, 'reason'):
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    elif hasattr(e, 'code'):
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
else:
    print("hello")
# everything is fine
