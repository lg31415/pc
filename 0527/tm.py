import requests

import json
import re
import time
import random
import sqlite3
import os
from bs4 import BeautifulSoup

db_path = "tm.sqlite"
if os.path.exists(db_path):
	# 每次进入都会删除数据
	os.remove(db_path)

# 创建数据库和表
conn = sqlite3.connect(db_path)  # 创建数据库
# 得到cursor对象
cursor = conn.cursor()  # 创建表
sql = """
create table sales_afu(
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
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
}


# 根据产品的id和页数得到某款产品的某页的评论
# 评论信息每页20条
def get_rate_list(itemId, currentPage):
	url = "https://rate.tmall.com/list_detail_rate.htm?itemId=" + str(
		itemId) + "&spuId=892999010&sellerId=2146516773&order=3&currentPage=" + str(
		currentPage) + "&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvt9vpvBOvUpCkvvvvvjiPPFSU1jYRRssZQjthPmPhAjiWPFFpljE8PLcWtjY8PLyCvvpvvhCvdphvmpvCduiNvvv%2Bv86Cvvyv9ZiPGvvvCsTjvpvhvUCvp8wCvvpvvhHhvphvC9mvphvvvbyCvm9vvhCvvvvvvvvvBBWvvvj2vvCHhQvv9pvvvhZLvvvCwpvvBBWvvvH1uphvmvvvpoE7RPCHkphvC9hvpyPO0vyCvhQmxhXVjwAwVty44Z7lK2kTKLBI74oQr3wgKFnfIWoZHd8rwkM6rE97RBBscGkQ%2Bu6XdeDHD76XdiT0f3TYQBoZHdUf85c6%2Bu0Xd3r%2F2QhvCPMMvvvtvpvhvvCvpvwCvva47rMNzv7HRphvCvvvphmrvpvEvvVSr7gvvhxf9phvHHiwjTFnzHi47Kxzt1177uB4NrGB&isg=BBgYpVP19_z-D9rJc2TGGsv36UZqqWmmQXMUtlIOL9Pk7bHX-hIaGUevISVdezRj&needFold=0&_ksTS=1527214206489_1338&callback=jsonp1339"

	try:

		response = requests.get(url, headers=headers)

		text = response.text
		print("text==",text)

		# 返回的评论信息
		text = response.text.replace("jsonp1339(", "").replace(")", "")
		# print("text===",text)
		python_dict = json.loads(text, encoding="utf-8")
		# print("python_dict==",python_dict)
		# 得到总页数
		# lastPage = python_dict["rateDetail"]["paginator"]["lastPage"]
		# print(lastPage)
		# #auctionSku胸罩的尺寸和颜色
		# auctionSku = python_dict["rateDetail"]["rateList"][0]["auctionSku"]
		# print('auctionSku==',auctionSku)
		# print(type(python_dict))
		return python_dict
	except Exception as e:
		print("请求出错了==url", url)
		print("请求出错了== e", e)
	return None


# 得到总页数
def get_total_page(itemId):
	try:
		tmalljson = get_rate_list(itemId, 1)
		total_page = tmalljson["rateDetail"]["paginator"]["lastPage"]
		return total_page
	except Exception as  e:
		print("出错了get_total_page==itemId==", itemId)
		print("出错了get_total_page==e==", e)
		return 0

#入口函数
def main():
	keyword = input("请输入您要爬虫商品类型:例如胸罩")
	#所有胸罩产品id
	product_id_list = get_product_id_list(keyword)
	#得到的id列表
	for id in product_id_list:
		# 99
		itemId = id
		print("正在爬虫itemId====",itemId)
		# 得到总页数
		total_page = get_total_page(itemId)

		page = 1
		while page < total_page:
			print("当前正在爬虫itemId==", itemId, "page==", page)

			try:
				# time.sleep(random.random() * 1)
				# 重新请求一次
				tmalljson = get_rate_list(itemId, page)
				rateList = tmalljson["rateDetail"]["rateList"]

				for item in rateList:
					# 颜色分类:黑色+象牙白;尺码:75A
					auctionSku = item["auctionSku"]
					auctionSku = re.split(r"[:;]", auctionSku)
					print("auctionSku==", auctionSku)
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

					# print("销售信息===",color,size,source,date,comment)

					sql = "INSERT INTO sales_afu(color,size,source,comment,date) VALUES ('%s','%s','%s','%s','%s');" % (
						color, size, source, comment, date)
					print(sql)
					# 执行sql语句
					cursor.execute(sql)
					# 提交事务
					conn.commit()

			except Exception as e:
				print("出错了e", e)
				continue

			page += 1

	# 关闭数据库
	cursor.close()
	conn.close()

#得到在搜索框输入胸罩的产品id列表
def get_product_id_list(keyword):

	url = "https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.4.52492beaYAxI9e&q="+str(keyword)+"&sort=d&style=g&from=mallfp..pc_1_searchbutton#J_Filter"
	print('-----------')
	response = requests.get(url,headers=headers)
	text = response.content
	# print("text==",text)
	soup = BeautifulSoup(text,"lxml")
	print(soup)
	links = soup.find_all(href=re.compile(r"//detail.tmall.com/item.htm"))
	links_list = []
	list_id = []
	for link in links:
		# print(link["href"])
		links_list.append(link["href"])
	#去重重复的链接
	links_list = list(set(links_list))
	#//detail.tmall.com/item.htm?id=547624680442&skuId=3482681907301
	for link in links_list:
		id = link.split("&")[0].replace("//detail.tmall.com/item.htm?id=","")
		print("id==",id)
		list_id.append(id)

		list_id = list(set(list_id))
	return list_id



if __name__ == "__main__":

	main()
	# get_rate_list("561578537531", 1)
	# print(get_product_id_list("充气娃娃"))