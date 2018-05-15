from urllib.request import HTTPHandler,Request,build_opener

def main():
    http_handler = HTTPHandler()
    opener = build_opener(http_handler)
    request = Request('http://atguigu.com/')
    response = opener.open(request)
    print(response.read().decode('utf-8'))


if __name__ == '__main__':
    main()