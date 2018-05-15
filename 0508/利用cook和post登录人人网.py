from urllib.request import build_opener,Request,HTTPCookieProcessor
from urllib import parse
from http.cookiejar import CookieJar

def main():
    #创建cookiejar对象，保存登录人人网的cookie
    cookiejar = CookieJar()
    http_cookie_process = HTTPCookieProcessor(cookiejar=cookiejar)
    #自定义opener
    openers = build_opener(http_cookie_process)
    openers.add_handler= [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36")]
    url = "http://www.renren.com/PLogin.do"
    data = {
        'email':"yangguangfu2017@163.com",'password':'fu123456',
    }
    data = parse.urlencode(data).encode('utf-8')
    request = Request(url,data=data,)
    response = openers.open(request)
    print(response.read().decode('utf-8'))
    print(cookiejar)

if __name__ == '__main__':
    main()