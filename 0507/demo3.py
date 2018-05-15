import urllib.request
from urllib.parse import urlencode

def main():
    url = 'http://httpbin.org/post'
    data = {'name':'kele','age':'20'}
    data = urlencode(data).encode('utf-8')
    html = urllib.request.urlopen(url,data=data)
    html_data = html.read()
    print(html_data.decode('utf-8'))

if __name__ == '__main__':
    main()