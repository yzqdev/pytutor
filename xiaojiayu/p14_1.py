import urllib.request

response = urllib.request.urlopen("http://img3.douban.com/view/photo/photo/public/p1955987961.jpg")
cat_img = response.read()

with open('cat_200_300.jpg', 'wb') as f:
    f.write(cat_img)
