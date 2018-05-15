# from urllib.request import ProxyHandler,build_opener,Request
#
# def main():
#     #创建代理对象
#     pro = ProxyHandler({'http':'1154718748:ibgcsea1@114.67.228.126:16816'})
#     #创建一个使用代理获取网页对象的工具
#     opener = build_opener(pro)
#
#     #创建请求对象
#     request = Request('http://www.baidu.com')
#     #使用请求对象请求数据并返回数据
#     response = opener.open(request)
#     print(response.read().decode('utf-8'))
import requests
def main():
    pro = {'http':'http://1154718748:ibgcsea1@114.67.228.126:16816/'}
    response = requests.get('http://www.baidu.com',proxies=pro)
    print(response.text)
if __name__ == '__main__':
    main()