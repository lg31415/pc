from bs4 import BeautifulSoup
import requests


url = "https://www.douyu.com/directory/all"
html = requests.get(url)

#创建对象
soup = BeautifulSoup(html.text,'lxml')

ellipsis_list = soup.select('h3[class="ellipsis"]')
# num_list = soup.select(".dy_num fr")

for ellipsis in ellipsis_list:
    print(ellipsis.get_text().lstrip())
# for num in num_list:
#     print(num.get_text())
