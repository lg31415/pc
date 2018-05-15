import requests


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
html = requests.get("http://music.163.com",headers=headers)
print(html.request)
print(html.headers)
print(html.encoding)