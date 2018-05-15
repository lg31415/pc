import requests
response12 = requests.get("http://www.atguigu.com/images/logo.jpg")
if response12.status_code == 200:
    with open('log.jpg','wb') as f:
        f.write(response12.content)