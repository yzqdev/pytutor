

start_urls = []
start = '1'

index = 0
for m in range(1, 217):
    url = 'http://qianfangzy.com/page/'
    url+=str(m)
    start_urls.append(url)
print(start_urls)
