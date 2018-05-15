from urllib.request import Request, urlopen
from urllib import parse
from lxml import etree
import os
import random

# https://tieba.baidu.com/f?kw=%E5%B0%9A%E7%A1%85%E8%B0%B750

# 写入文件函数
'''
b:html文件
file_name:文件名
srt1:所进入的吧名
'''


def pag_write(b, file_name, str1):
    with open(file_name + '.html', 'wb') as f:
        f.write(b)
        print(b)
        print('正在下载' + str1, file_name)


'''
url ：拼接完成的浏览器能够识别的贴吧url路径
un_hander:浏览器标识
html:服务器返回向对应的浏览器请求的数据因为没有填写date所以默认为get请求
a:返回服务器响应的类文件对象
b:类文件对象支持文件的操作，read读取全部的内容，返回的是字符串
'''
num = 1

def wirite_img(img_url):
    img_a = Request(img_url)
    response = urlopen(img_a)
    img_content = response.read()

    if not os.path.exists('./img/'):
        os.mkdir("./img/")
    global num
    with open("./img/第"+str(num)+"张.jpg","wb") as f:
        f.write(img_content)
    num+=1
def image_link(tz_link):
    html = Request(tz_link)
    response = urlopen(html)
    img_link = response.read()
    img_s = etree.HTML(img_link)
    img_url = img_s.xpath('//div[@class="d_post_content j_d_post_content "]/img[@class="BDE_Image"]/@src')
    #print(img_url)
    for img_l in img_url:
        wirite_img(img_l)

def link_list(b):
    html = etree.HTML(b)
    url = html.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
    for u in url:
        tz_link = "https://tieba.baidu.com/"+u
        #print(tz_link)
    #print(html)
        image_link(tz_link)
def pag_dow(file_name, url, str1):
    un_hander = [
        {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"},
        {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0"},
                 ]
    un_hander1 = random.choice(un_hander)
    html = Request(url)
    #html.add_header('User-Agent', un_hander1['User-Agent'])
    a = urlopen(html)
    b = a.read().decode("utf-8")
    #print(b)
    #获取帖子链接
    link_list(b)
    #pag_write(b, file_name, str1)



# 拼接URL
def baidu_pj(url, start_pag, end_pag, str1):
    for a in range(start_pag, end_pag + 1):
        b = (a - 1) * 50
        url = url + '&ie=utf-8&pn=' + str(b)
        file_name = str1 + '第' + str(a) + '页'
        pag_dow(file_name, url, str1)


def main():
    str1 = input("请输入您要访问的贴吧：")
    start_pag = int(input("请输入您要访问的起始页："))
    end_pag = int(input('请输入您要访问的末页：'))
    wd = {'kw': str1}
    # 把对应的字典数据进行转吧使浏览器能够识别
    kw = parse.urlencode(wd)
    # 把贴吧名字进行转码能够让浏览器识别
    url = 'https://tieba.baidu.com/f?' + kw
    # 拼接浏览器URL函数
    baidu_pj(url, start_pag, end_pag, str1)


if __name__ == '__main__':
    main()
