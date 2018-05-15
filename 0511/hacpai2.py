from bs4 import BeautifulSoup
from lxml import etree
import requests
import re

h = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'}
html = requests.get("https://hacpai.com/recent",headers=h)
#print(html.text)
#pc = etree.HTML(html.text)
html = html.text

soup = BeautifulSoup(html,'lxml')


#print(soup.prettify())
#print(soup.div['class'])
#print(soup.a['href'])
#print(soup.p.string)
# p_list= soup.find_all()
# print(p_list.text)
#print(soup.p.string)
# p_list = soup.find_all(name='p')
# print(p_list)
# for p in p_list:
#     print(p.string)
#print(soup.head.contents)
# print(soup.find_all('b'))
# for tag in soup.find_all(re.compile("^H")):
#     print(tag.name)
# print(soup.find_all(['d','a']))
# print(soup.find_all(id="icomoon-ignore"))
# print(soup.find_all(text=re.compile(r'最')))
h_list = soup.find_all(href=re.compile(r'https://hacpai.com/'))
for list in h_list:
    print(list['href'])
