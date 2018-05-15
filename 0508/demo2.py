from urllib.request import HTTPHandler,Request,build_opener

#创建
http = HTTPHandler()
#创建opener
opener = build_opener(http)

url = 'http://www.baidu.com'
#返回浏览器request
b = Request(url)
#返回response
a = opener.open(b)

#读取全部数据
data = a.read()

print(data.decode('utf-8'))