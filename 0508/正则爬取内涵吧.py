from urllib.request import urlopen,Request
import zlib
from urllib import parse

class Requests(object):
    def load_pag(self,pag):
        url = 'http://d2.sku117.biz/pw/thread.php?fid=5&page='+str(pag)
        un = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
        html = Request(url,headers=un)

        response2 = urlopen(html)
        return response2.read()

if __name__ == '__main__':
    re = Requests()
    con = re.load_pag(1)
    print(con.decode('utf-8'))
