import requests
from lxml import etree

def main():
    h = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
    html = requests.get("https://hacpai.com/recent",headers=h)
    #print(html.text)
    pc = etree.HTML(html.text)
    content = pc.xpath('//h2[@class="article-list__title"]/a/text()')
    print(content)
    for i in content:
        print(i)
    content1 = pc.xpath('//h2[@class="article-list__title"]/a/@href')
    for s in content1:
        print(s)
if __name__ == '__main__':
    main()