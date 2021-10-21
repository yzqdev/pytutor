import urllib.request

response = urllib.request.urlopen("https://doc.shiyanlou.com/document-uid731737labid7100timestamp1531381084391.png/wm")
cat_img = response.read()

if __name__ == '__main__':
    with open(r'D:\temp\cat_200_300.jpg', 'wb') as f:
        f.write(cat_img)
        print("生成完毕")
