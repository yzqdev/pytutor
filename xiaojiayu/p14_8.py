import urllib.request
import random

url = 'http://www.whatismyip.com.tw/'

print("添加代理ip地址（ip:端口号），多个ip地址间用英文的分号隔开！")
iplist = input("请开始输入：").split(sep=";")

while True:
    ip = random.choice(iplist)
    proxy_support = urllib.request.ProxyHandler({'http': ip})

    opener = urllib.request.build_opener(proxy_support)
    opener.addheaders = [('User-Agent',
                          'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')]

    urllib.request.install_opener(opener)

    try:
        print("正在尝试使用 %s 访问..." % ip)
        response = urllib.request.urlopen(url)
    except urllib.error.URLError:
        print("访问出错！")
    else:
        print("访问成功！")

    if input("请问是否继续？（Y/N）") == 'N':
        break
