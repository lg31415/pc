from urllib.request import urlopen,Request,URLError

url = 'http://www.zhangux.com'
request = Request(url)
try:
    html = urlopen(request)
except URLError as e :
    print(e)
else:
    print(html.read().decode('utf-8'))