from urllib.request import build_opener,HTTPCookieProcessor,Request
from http.cookiejar import CookieJar,MozillaCookieJar

#创建一个cookiejar对象，产生的cookie就会保存在cookiejar对象里面
cook = CookieJar()
handerl_cookie_process = HTTPCookieProcessor(cookiejar=cook)
#创建opener对象，传入handler处理器
opener = build_opener(handerl_cookie_process)
url = 'http://www.baiadu.com'
response = opener.open(url)

print(response.read())