from urllib.request import Request,urlopen
from urllib import parse


def pag_write(html,file_name):
    with open(file_name+'.html','wb') as f:
        f.write(html)
        print(file_name,'下载完毕')


def pag_down(new_url,file_name):
    print("正在下载",file_name)
    un_hearder  =  {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    request = Request(new_url,headers=un_hearder)
    response = urlopen(request)
    html = response.read()
    pag_write(html,file_name)

def baidu_pj(url,start_age,end_age,wd):
    for n in range(start_age,end_age+1):
        m = (n-1)*50
        new_url = url + '&ie=utf-8&pn=' + str(m)
        file_name = wd + '第' + str(n) +'页'
        pag_down(new_url,file_name)


def main():
    wd = input("请输入您要访问的贴吧")
    start_age = int(input("起始："))
    end_age = int(input("结束:"))
    pd = {'kw':wd}
    url = 'https://tieba.baidu.com/f?'
    kw = parse.urlencode(pd)
    url = url + kw
    baidu_pj(url,start_age,end_age,wd)

if __name__ == '__main__':
    main()