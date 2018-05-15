from urllib.request import urlopen,Request
from lxml import etree
import re
class Requests(object):

    def load_pag(self,pag):
        print("正在下载%s页" % pag)
        url = "http://www.neihanpa.com/article/list_5_"+str(pag)+".html"
        un = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
        html = Request(url,headers=un)

        response2 = urlopen(html)
        return response2.read()

    def print_one_page(self,item_pag,pag):
        print("正在打印%s页段子" % pag)
        for item in item_pag:
            item = item.replace('<div class="f18 mb20">', "") \
                .replace('</div>', "").replace('<p>', ""). \
                replace('</p>', "").replace('<br />', ""). \
                replace('&ldquo;', "").replace('&ldquo;', "") \
                .replace("&hellip;", "").replace("&rdquo;", "")
            print(item)
            self.write_pag(item,pag)

    def write_pag(self,con,pag):
        print("正在下载%s页的段子" % pag)
        with open('内涵段子第'+str(pag)+'页.txt','a') as f:
            f.write(con)

if __name__ == '__main__':
    print('''
    ===============
        内涵小爬虫
    ===============
    ''')
    print("按enter开始")
    input()
    rep = Requests()
    con = rep.load_pag(1).decode('gb2312')
    html = etree.HTML(con)
    result = html.xpath('//div[@class="f18 mb20"]/p/text()|//div[@class="f18 mb20"]/text()')
    print(result)
