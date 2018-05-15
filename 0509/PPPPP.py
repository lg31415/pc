from urllib.request import urlopen,Request
from lxml import etree
import os
import requests
num = 1


def open_img_url(img_url):
    global num
    request = requests.get(img_url,proxies={'https':'socks5://127.0.0.1:1086'})
    if not os.path.exists("./img/"):
        os.makedirs("./img/")
    with open("./img/图片"+str(num)+"张.jpg") as f:
        f.write(request.content)
    num+=1
    print("111")

def open_first(one_url):
    print(one_url)
    request = requests.get(one_url,proxies={'https':'socks5://127.0.0.1:1086'})
    html = etree.HTML(request.text)
    img_url = html.xpath('//div[@class="_2dr5P4z"]//div[@class="_1jNYw94"]/img/@src')
    for i in img_url:
        open_img_url(i)


def index_one(index_url):
    handler = {
        'Authority': 'www.pixiv.net',
        'Method': 'GET',
        'Path': '/showcase/',
        'Scheme': 'https',
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh,zh-CN;q=0.9,en;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6",
        "cache-control": "max-age=0",
        "cookie": "p_ab_id=6; p_ab_id_2=2; __utmz=235335808.1525766549.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=30509203_fd7f8192da2c6a43b8d43f378cd2ec86; device_token=2fb9a2aa63a0cce315f78aea1f09cacb; c_type=9; a_type=0; b_type=1; yuid=JoM4Jlc33; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=30509203=1^9=p_ab_id=6=1^10=p_ab_id_2=2=1^11=lang=en=1; __gads=ID=c0395711d3ca5f3f:T=1525766552:S=ALNI_Mb0loMHplobAqT772jCF7JHttC70A; is_sensei_service_user=1; __utmc=235335808; _ga=GA1.2.1784901121.1525766549; _gid=GA1.2.94435904.1525860928; __utma=235335808.1784901121.1525766549.1525860917.1525863326.4; module_orders_mypage=%5B%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22showcase%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; tag_view_ranking=RTJMXD26Ak~jhuUT0OJva~Lt-oEicbBr~T4PSuIdiwS~DlBi_h7Pbj~q303ip6Ui5~DHzITAK37t~MPcKWMDzOj~9LhLC1Kxwa~Ix912GkxZw~nneK_PMY0e~vKaV_Lyk9X~dVHTSCIxW9~1AJ13XKtef~VN7cgWyMmg~RAjfbf58gz~PZplhsP9oO~mO0Da-IPL4~SDTUmCwiZx~nJibHcWHjR~2V0-EgyHVg~HHQeBgH4mi~Xyw8zvsyR4~aKhT3n4RHZ~-Lny-nXdRn; __utmt=1; __utmb=235335808.28.10.1525863326",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }
    html_one = requests.get(index_url,headers=handler,proxies={'https':'socks5://127.0.0.1:1086'})
    print(html_one.text)
    html_one = etree.HTML(html_one.text)
    print(html_one)
    one_url = html_one.xpath('//div[@class="_2RuXgvM"]/a[@class="_2ky0mEq"]/@href')
    print(one_url)
    for i in one_url:
        one_url = "https://www.pixiv.net/" + i
    open_first(one_url)
def main():
    handler = {
        'Authority': 'www.pixiv.net',
        'Method':'GET',
        'Path': '/',
        'Scheme': 'https',
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        #"accept-encoding": "gzip, deflate, br",
        "accept-language": "zh,zh-CN;q=0.9,en;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6",
        "cache-control": "max-age=0",
        "cookie": "p_ab_id=6; p_ab_id_2=2; __utmz=235335808.1525766549.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); PHPSESSID=30509203_fd7f8192da2c6a43b8d43f378cd2ec86; device_token=2fb9a2aa63a0cce315f78aea1f09cacb; c_type=9; a_type=0; b_type=1; yuid=JoM4Jlc33; login_ever=yes; __utmv=235335808.|2=login%20ever=yes=1^3=plan=normal=1^5=gender=male=1^6=user_id=30509203=1^9=p_ab_id=6=1^10=p_ab_id_2=2=1^11=lang=en=1; __gads=ID=c0395711d3ca5f3f:T=1525766552:S=ALNI_Mb0loMHplobAqT772jCF7JHttC70A; is_sensei_service_user=1; __utmc=235335808; _ga=GA1.2.1784901121.1525766549; _gid=GA1.2.94435904.1525860928; __utma=235335808.1784901121.1525766549.1525860917.1525863326.4; module_orders_mypage=%5B%7B%22name%22%3A%22tag_follow%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22showcase%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22recommended_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sketch_live%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22everyone_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22following_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22mypixiv_new_illusts%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22fanbox%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22featured_tags%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22contests%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22user_events%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22sensei_courses%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22spotlight%22%2C%22visible%22%3Atrue%7D%2C%7B%22name%22%3A%22booth_follow_items%22%2C%22visible%22%3Atrue%7D%5D; tag_view_ranking=RTJMXD26Ak~jhuUT0OJva~Lt-oEicbBr~T4PSuIdiwS~DlBi_h7Pbj~q303ip6Ui5~DHzITAK37t~MPcKWMDzOj~9LhLC1Kxwa~Ix912GkxZw~nneK_PMY0e~vKaV_Lyk9X~dVHTSCIxW9~1AJ13XKtef~VN7cgWyMmg~RAjfbf58gz~PZplhsP9oO~mO0Da-IPL4~SDTUmCwiZx~nJibHcWHjR~2V0-EgyHVg~HHQeBgH4mi~Xyw8zvsyR4~aKhT3n4RHZ~-Lny-nXdRn; __utmt=1; __utmt_p=1; __utmb=235335808.37.9.1525868231544",
        'referer': 'https://www.pixiv.net/showcase/',
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }
    #request = Request("https://www.pixiv.net",headers=handler)
    #response = urlopen(request)
    response = requests.get("https://www.pixiv.net",headers=handler,proxies={'https':'socks5://127.0.0.1:1086'})
    html = etree.HTML(response.text)
    index_url = html.xpath('//section[@class="item showcase "]//ul[@class="more"]/li/a/@href')
    str = index_url[0]
    index_url = "https://www.pixiv.net"+str
    print(index_url)
    index_one(index_url)



if __name__ == '__main__':
    main()