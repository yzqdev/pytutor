import urllib.request

url = 'http://www.whatismyip.com.tw/'

proxy_support = urllib.request.ProxyHandler({'http': '211.138.121.38:80'})

# 接着创建一个包含代理ip的opener
opener = urllib.request.build_opener(proxy_support)

# 安装进默认环境
urllib.request.install_opener(opener)

# 试试看ip地址改了没
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)
