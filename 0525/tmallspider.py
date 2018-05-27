import requests
import json
import re
import time
import random
import sqlite3
import os
from bs4 import BeautifulSoup

db_path = "bra_all"
if os.path.exists(db_path):
    os.remove(db_path)

# 创建数据库和表
conn = sqlite3.connect(db_path)

# 得到cursor对象
cursor = conn.cursor()

sql = """
create table sql_tm(
id integer primary key autoincrement not null,
color text not null,
size text not null,
source text not null,
comment text not null,
date text not null
);
"""
cursor.execute(sql)
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
}


def get_rate_list(itemId, currentPage):
    try:
        url = "https://rate.tmall.com/list_detail_rate.htm?itemId="+str(itemId)+"&spuId=892999010&sellerId=2146516773&order=3&currentPage="+str(currentPage)+"&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvuQvPvBOvUvCkvvvvvjiPPFSUtjnbPFs96j1VPmP9QjYUP2c91jYVnLMU6j1bdphvmpvWAUloZ9CZPIwCvvpvCvvviQhvCvvv9UUPvpvhvv2MMqyCvm9vvvvxphvv5vvvv%2BlvpvsHvvm2phCvhRvvvUnvphvpkvvvv%2Blvpv1buphvmvvv9bj4QmuMkphvC99vvOH0pvyCvhQUWHgvC0Ersj7Q%2BulsbSLXS4ZAhjCwD7zWaXTAVArl%2BWe9eEr%2Bm7zWa4p7%2B3%2BiaNoxfXkKfvc61WFyeED%2BVd0DyOvO5onmsX7vAEyavphvC9vhvvCvp2yCvvpvvvvv9phvHHiafbv%2FjHi47526ts1IcU34raGBRphvCvvvvvmrvpvEvvQ62fKqvWoz9phvHHiaMqCazHi47IqAt1Q47MC4NrGBRphvCvvvvvv%3D&isg=BBwcu6NfqydJIV4GlBZlA4Wv7TwOPdWZbC54nfYdHYfCQb7LHqWQT5JDpaG5SfgX&needFold=0&_ksTS=1527298834389_1043&callback=jsonp1044"
        print(url)
        response = requests.get(url, headers=headers)
        text = response.text
        print(text)
        # 返回评论的信息
        text = text.replace("jsonp1044(", "").replace(")", "")

        python_dict = json.loads(text, encoding='utf-8')
        print(python_dict)
        return python_dict
    except Exception as a:
        print('出错了', a)
        return 0


# 得到总页数
def get_all_page(itemId):
    try:
        tmalljson = get_rate_list(itemId, 1)
        total_page = tmalljson["rateDetail"]["paginator"]["lastPage"]
        return total_page
    except Exception as e:
        print("出错了")
        return 0


# 入口函数
def main():
    keyword = input("请输入您要爬虫商品类型:")
    id_list = get_product_id_list(keyword)
    for id in id_list:
        itemId = id
        page = 1
        pages = get_all_page(itemId)

        while page < pages:
            print(page)
            print(pages)
            python_text = get_rate_list(itemId, page)

            list = python_text['rateDetail']['rateList']
            for item in list:
                # 颜色分类:黑色+象牙白;尺码:75A
                auctionSku = item["auctionSku"]
                auctionSku = re.split(r"[:;]", auctionSku)
                # print("auctionSku==", auctionSku)
                # 胸罩的颜色,肤色
                color = auctionSku[1]
                # 尺寸'75A,70C
                size = auctionSku[3]
                # 来自的平台-天猫
                source = item["cmsSource"]
                # 评论内容
                comment = item["rateContent"]
                # 评论的时间
                date = item["rateDate"]
                sql = "INSERT INTO sql_tm(color, size, source, comment, date) VALUES ('%s','%s','%s','%s','%s');" % (color, size, source, comment, date)
                print(sql)
                cursor.execute(sql)
                conn.commit()
            page += 1


# 得到在搜索框输入胸罩的产品id列表
def get_product_id_list(keyword):
    url = "https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.4.52492beaYAxI9e&q=" + str(
        keyword) + "&sort=d&style=g&from=mallfp..pc_1_searchbutton#J_Filter"
    response = requests.get(url, headers=headers)
    text = response.content
    # print("text==",text)
    soup = BeautifulSoup(text, "lxml")
    links = soup.find_all(href=re.compile(r"//detail.tmall.com/item.htm"))
    links_list = []
    list_id = []
    for link in links:
        # print(link["href"])
        links_list.append(link["href"])
    # 去重重复的链接
    links_list = list(set(links_list))
    # //detail.tmall.com/item.htm?id=547624680442&skuId=3482681907301
    for link in links_list:
        id = link.split("&")[0].replace("//detail.tmall.com/item.htm?id=", "")
        # print("id==",id)
        list_id.append(id)

        list_id = list(set(list_id))
    return list_id


if __name__ == '__main__':
    # get_rate_list(44361449416, 1)
    main()
    cursor.close()
    conn.close()
