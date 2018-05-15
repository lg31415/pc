import requests

html = requests.get('http://dynamic-image.yesky.com/740x-/uploadImages/2016/338/41/IB4U757R80PQ.jpg')
if html.status_code == 200:
    with open('meinv.jpg','wb') as f:
        for block in html.iter_content(1024):
            if not block:
                break
            f.write(html.content)