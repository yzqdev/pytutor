import urllib.request
import urllib.parse
import json
import time

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"

while True:
    content = input('请输入待翻译内容(输入"q!"退出程序)：')
    if content == 'q!':
        break

    data = {}
    data['type'] = 'AUTO'
    data['i'] = content
    data['doctype'] = 'json'
    data['xmlVersion'] = '1.6'
    data['keyfrom'] = 'fanyi.web'
    data['ue'] = 'UTF-8'
    data['typoResult'] = 'true'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url, data)
    req.add_header('Referer', 'http://fanyi.youdao.com')
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36X-Requested-With:XMLHttpRequest')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    target = json.loads(html)
    print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))

    time.sleep(5)
