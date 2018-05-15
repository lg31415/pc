from urllib.request import Request,build_opener,ProxyBasicAuthHandler,HTTPPasswordMgrWithDefaultRealm


http_mgr_real = HTTPPasswordMgrWithDefaultRealm()

user = 'sunfengchun'
passwd = 'sunfengchun'

pro = '97.64.107.241:8899'

http_mgr_real.add_password(None,pro,user,passwd)


pro_auth = ProxyBasicAuthHandler(http_mgr_real)

opener = build_opener(pro_auth)

request = Request('http://www.baidu.com')

response = opener.open(request)
print(response.read().decode('utf-8'))