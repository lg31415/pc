import requests
import re

#c = '20180416_meizitu_01'
#c = "http://ac.meijiecao.net/ac/img/znb/meizitu/20180416_meizitu_0"+str(a)+".jpg"

#d = re.sub(r'^2018.*',c,)
#print(d)
for a in range (9):

    b = requests.get("https://www.pixiv.net/member_illust.php?mode=medium&illust_id=68617411")
    with open(str(a)+'.jpg','wb') as f:
        f.write(b.content)