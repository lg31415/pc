from urllib3 import PoolManager,disable_warnings
import re
from bs4 import BeautifulSoup



def get_headers():
    headers = {
     'authority':'gm.mmstat.com',
     'method':'GET',
     'path':'/tmallbrand.99.2?r1526018595633=1',
     'scheme':'https',
     "accept":"image/webp,image/apng,image/*,*/*;q=0.8",
     "accept-encoding":"gzip, deflate, br",
     "accept-language":"zh,zh-CN;q=0.9,en;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6",
     "cookie":"cna=AjF3EzXpoHwCAXlFUaa/Y3JS; cap=effc; sca=293c858f; atpsida=e4901092d275fddc0628b178_1526018587_1; cad=kZ8GFzDAabbbJK7bokBJ7MzwBDHmEkomIhJPj0c5VKI=0001",
     "referer":"https://www.tmall.com/?ali_trackid=2:mm_26632258_3504122_55934697:1526018586_213_332700509&clk1=1e67a4525221f8094d8530330c7454d7&upsid=1e67a4525221f8094d8530330c7454d7",
     "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
    }

    return headers

def get_product_id_list():
    url = "https://list.tmall.com/search_product.htm?q=%D0%D8%D5%D6&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&from=mallfp..pc_1_searchbutton&smToken=7784c0cb3f664586b60eb140eddbc544&smSign=XnBIrCJRsPQoAsWokYTxGg%3D%3D"
    http = PoolManager()
    headers = get_headers()
    request = http.request("GET",url,headers=headers)
    result = request.data.decode('GBK')

    link_list = []
    id_list = []
    soup = BeautifulSoup(result,'lxml')
    tags = soup.find_all(href=re.compile(r'detail.tmall.com/item.htm'))
    for tag in tags:
        print(tag['href'])
        link_list.append(tag['href'])


    link_list = list(set(link_list))


    for link in link_list:
        link = link.split("&")[0]
        id = link.replace("//detail.tmall.com/item.htm?id=","")
        id_list.append(id)

    return id_list
print(get_product_id_list())
