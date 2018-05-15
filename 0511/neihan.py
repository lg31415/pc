import re
import requests
import json
import jsonpath
from lxml import etree

def main():
    url = "http://www.qiushibaike.com/8hr/page/1"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/65.0.3325.146 Safari/537.36"}
    html = requests.get(url,headers=headers)
    #print(html.text)
    #转换成dom对象
    dom = etree.HTML(html.content)
    #进行xpath的到包含段子的div
    index = dom.xpath("//div[contains(@id, 'qiushi_tag_')]")
    #print(index)
    all_con = []
    for i in index:
        item_dic = {}
        #图片链接
        img_url = i.xpath('.//div/a/img[@class="illustration"]/@src')
        #用户姓名
        user_name = i.xpath('.//div//h2/text()')
        #内容
        content = i.xpath('.//a/div/span/text()')
        #点赞
        love = i.xpath('.//div/span/i/text()')
        #评论
        talk = i.xpath('.//div/span/a/i/text()')
        if len(img_url) > 0:
            item_dic['img_url'] = img_url[0].replace('\\n','')
        if len(user_name) > 0:
            item_dic['name'] = user_name[0].replace('\\n','')
        if len(content) > 0:
            item_dic['content'] = content[0].replace('\\n','')
        if len(love) > 0:
            item_dic['love'] = love[0].replace(r'\n','')
        if len(talk) > 0:
            item_dic['talk'] = talk[0].replace(r'\n','')

        print(item_dic)
        all_con.append(item_dic)
    f = open("qsbk.json",'w',encoding="utf-8")
    json.dump(all_con,f,ensure_ascii=False)
    print("OK")

if __name__ == '__main__':
    main()