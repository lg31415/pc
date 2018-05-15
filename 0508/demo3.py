from urllib.request import urlopen,Request


def main():
    un_hander = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

        "Accept-Language":"zh,zh-CN;q=0.9,en;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "Cookie":"BAIDUID=EAF4150572577AD24CC1FBDC69AD4141:FG=1; PSTM=1525689552; H_PS_PSSID=; BIDUPSID=67CA2B946A90C4484E952EC0B7FDB3F2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDUSS=FGQXhCejYtdFBWUC1lbFR-MjhUVnFMeExjM3BHU2ZiUGVuTnZUcFA1dn5oeGhiQVFBQUFBJCQAAAAAAAAAAAEAAACH9Q4pv8DA1gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP~68Fr~-vBacD; BDSFRCVID=pLIsJeCCxG39reoAPjNfDf2490CH6AQX2liC3J; H_BDCLCKID_SF=tbkD_C-MfIvhDRTvhCcjh-FSMgTBKI62aKDsQpRY-hcqEpO9QT-BK4LeLJ3BWt5R5JuJVCJnWIQNVfP4h-rTDUTh-p52f6tDfnuj3J; PSINO=1; PHPSESSID=a98qbbiv35ac51abnv8mhrn2r2; Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1525752654; Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1525752654",
        "Host":"i.baidu.com",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }
    url = 'http://i.baidu.com/'
    request = Request(url,headers=un_hander)
    response = urlopen(request)
    print(response.read().decode('utf-8'))

if __name__ == '__main__':
    main()

