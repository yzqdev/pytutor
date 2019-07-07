import urllib.request
import urllib.parse
import json

content = input("请输入需要翻译的内容：")

url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"

head = {}
head['Referer'] = 'http://fanyi.youdao.com'
head[
    'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36X-Requested-With:XMLHttpRequest'

data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data, head)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
target = json.loads(html)

print("翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
