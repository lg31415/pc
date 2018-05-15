from urllib.request import Request,urlopen,HTTPError

url = 'http://baidu.com/itcast/index.html'
request = Request(url)
try:
    html = urlopen(request)
except HTTPError as r:
    print (r.code)
# else:
#     print(html.read().decode('utf-8'))