import requests
import lxml
from bs4 import BeautifulSoup

url = "https://hr.tencent.com/position.php?lid=2156"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/65.0.3325.146 Safari/537.36"}

html = requests.get(url,headers=headers)
#print(html.text)

soup = BeautifulSoup(html.text,'lxml')

cont = soup.select('tr[class="even"]')
print(cont)
for i in cont:
    name = i.get_text()
    url = i.select('a[href]')[0]['href']
    print(name)
cont = soup.select('tr[class="odd"]')
print(cont)
for i in cont:
    name1 = i.get_text()
    url1 = i.select('a[href]')[0]['href']
    print(name1)
#cont1 = soup.select('td')
#print(cont1)
