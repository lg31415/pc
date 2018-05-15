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
# print(soup.select('title'))
# print(soup.select('a'))
# print(soup.select('b')
#通过类名查找
#print(soup.select(".xxx"))
#通过id查找
# print(soup.select("#xxx"))
#组合查找
# print(soup.select("p #xxx"))
#直接子标签查找，则使用 > 分隔
# print(soup.select("head > title"))
#属性查找
# print(soup.select("a[class='xxx']"))
#属性的组合查找
# print(soup.select(‘p a[href=“xxx”]’))
#获取内容
# print(soup.select('title')[0].get_text())
# for title in soup.select('title'):
#     print(title.get_text())
# list = soup.select('p')
# for i in list:
#     print(i.get_text())
