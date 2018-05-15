import requests


def main():
    hander = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit \
                    /537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image \
                    /webp,image/apng,*/*;q=0.8',
        #'Accept-Encoding': 'gzip, deflate',
        #'Accept-Language': 'zh-CN, zh; q=0.9',
        'Referer': 'http://www3.uptorrentfilespacedownhostabc.info/updowm/file.php/P22OGZq.html',
        # 'Origin': 'http://www3.uptorrentfilespacedownhostabc.info',
        'Upgrade-Insecure-Requests': '1',
        'Host': 'www3.uptorrentfilespacedownhostabc.info',
    }
    data = {
        'type': 'torrent',
        'id': 'P22OGZq',
        'name': '55d19496b8995be1f2c1118daa47ba4c4c8b98ec'
    }
    url = 'http://www3.uptorrentfilespacedownhostabc.info/updowm/down.php'
    response = requests.post(url,headers=hander,data=data)
    if response.status_code == 200:
        with open('1.txt','wb') as f:
            f.write(response.content)
    else:
        print(response.status_code)
if __name__ == '__main__':
    main()