from urllib.request import Request,urlopen
import ssl


def main():
    sslcontent = ssl._create_unverified_context()
    url = "http://www.12306.cn/mormhweb"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    request = Request(url,headers=headers)
    reponse = urlopen(request,context=sslcontent)
    print(reponse.read().decode('utf-8'))

if __name__ == '__main__':
    main()