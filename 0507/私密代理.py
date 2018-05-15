from urllib.request import ProxyHandler,Request,build_opener

#创建代理处理对象
pro_h = ProxyHandler({'http':'ali.b.mansora.net:6111'})

#创建一个opper对象
o = build_opener(pro_h)

#创建一个request对象
request = Request('http://www.baidu.com/')

a = o.open(request)
print(a.read().decode('utf-8'))