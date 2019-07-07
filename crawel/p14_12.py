from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
someurl="https://www.baidu.com"
req = Request(someurl)

try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else:
    pass
# everything is fine
