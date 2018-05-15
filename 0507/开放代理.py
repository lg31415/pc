from urllib.request import ProxyHandler,build_opener,Request

#构建两个代理一个有代理ip一个没有代理ip
httppro = ProxyHandler({'http':'122.72.18.34:80'})
httpprp1 = ProxyHandler({})

#定义代理开关
proS = False
if proS:
    o = build_opener(httppro)
else:
    o = build_opener(httpprp1)

request = Request("http://www.baidu.com/")
response = o.open(request)

print(response.read().decode('utf-8'))