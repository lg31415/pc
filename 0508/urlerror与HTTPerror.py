from urllib.request import Request,urlopen,URLError


#URLError没有网络的时候报错

def main():
    try:
        url = "http://www.baidu.com"
        request = Request(url)
        response = urlopen(request)

    except URLError as e:
        print(e)
    else:
        #正常执行
        print(response.read().decode('utf-8'))


if __name__ == '__main__':
    main()