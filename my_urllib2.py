import urllib.request

url = "http://www.baidu.com"

print('第一种方法')

response_o = urllib.request.urlopen(url)
print(response_o.getcode())

htmlcontent = response_o.read()
print(len(htmlcontent))



