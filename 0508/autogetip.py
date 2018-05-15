# from urllib.request import ProxyHandler,build_opener,Request
# import random
# #创建代理对象
# proxy_list = [
#     {"http":"14.113.126.83:80"},
#     {"http":"114.113.126.86:80"},
#
# ]
#
# http_pro = random.choice(proxy_list)
# pro = ProxyHandler(http_pro)
# #创建打开工具
# opener = build_opener(pro)
# #创建请求
# request = Request('http://www.baidu.com')
# response = opener.open(request)
# print(response.read().decode('utf-8'))
import requests
import random

pro_list = [
    {"http":"116.231.8.154:53281"},
    {"http":"101.37.79.125:3128"},
    ]
pro = random.choice(pro_list)

html = requests.get('http://www.baidu.com',proxies=pro)
print(html.text)