import urllib.request
import re


def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36')
    page = urllib.request.urlopen(req)
    html = page.read().decode('utf-8')

    return html


def get_img(html):
    print("hello")
    p = r'<img class="BDE_Image" src="[^"]*\.jpg"'
    imglist = re.findall(p, html)

    for each in imglist:
        print(each)
    print("end")


if __name__ == '__main__':
    url = "http://tieba.baidu.com/p/6186074710"
    get_img(open_url(url))
