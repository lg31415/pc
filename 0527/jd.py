import requests
import json
import re
import sqlite3
from bs4 import BeautifulSoup
proxy = {"http": "http://trygf521:a4c4avg9@122.114.247.216:16817/"}
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
}

db_path = "jd.sqlite"

# 创建数据库和表
conn = sqlite3.connect(db_path)  # 创建数据库
# 得到cursor对象
cursor = conn.cursor()  # 创建表

# 根据产品的id和页数得到某款产品的某页的评论
# 评论信息每页20条
def get_rate_list(itemId, currentPage):
	# url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv234&productId=6673004&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1"
	url = "https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv234&productId="+str(itemId)+"&score=0&sortType=5&page="+str(currentPage)+"&pageSize=10&isShadowSku=0&rid=0&fold=1"

	try:
		response = requests.get(url,headers=headers)
		print(response.text)
		# # 返回的评论信息
		text = response.text.replace("fetchJSON_comment98vv234(", "").replace(");", "")
		print("text===",text)
		python_dict = json.loads(text, encoding="utf-8")
		return python_dict
	except Exception as e:
		print("请求出错了==url", url)
		print("请求出错了== e", e)
	return None

# # 得到总页数
def get_total_page(itemId):
	try:
		jdjson = get_rate_list(itemId, 1)
		total_page = jdjson["maxPage"]
		return total_page
	except Exception as  e:
		print("出错了get_total_page==itemId==", itemId)
		print("出错了get_total_page==e==", e)
		return 0


#入口函数
def main():
	product_id_list = get_product_id_list("胸罩")
	for id in product_id_list:
		#产品的id
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
				jdjson = get_rate_list(itemId, page)
				comments = jdjson["comments"]

				for item in comments:
					# 胸罩的颜色,肤色
					color = item["productColor"]
					# 尺寸'75A,70C
					size = item["productSize"]
					# 来自的平台-京东
					source = "京东"
					# 评论内容
					comment = item["content"]
					# 评论的时间
					date = item["creationTime"]
					print(color,size,source,date,comment)

					sql = "INSERT INTO sales_afu(color,size,source,comment,date) VALUES ('%s','%s','%s','%s','%s');" % (
						color, size, source, comment, date)
					print(sql)

					cursor.execute(sql)
					conn.commit()#提交事务


			except Exception as e:
				print("出错了e", e)
				continue#出错了,重新请求

			page += 1

#得到在搜索框输入胸罩的产品id列表
def get_product_id_list(keyword):
	url = "https://search.jd.com/Search?keyword="+str(keyword)+"&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&psort=3&click=0"
	try:
		response = requests.get(url,headers=headers)
		text = response.text
		# print("text==",text)
		soup = BeautifulSoup(text,"lxml")
		links = soup.find_all(href=re.compile(r"//item.jd.com/"))
		links_list = []
		list_id = []
		for link in links:
			# print(link["href"])
			links_list.append(link["href"])
		#去重重复的链接
		links_list = list(set(links_list))
		# //item.jd.com/6356792.html#comment
		for link in links_list:
			id = link.split("com/")[1].replace(".html","").replace("#comment","")
			# print("id==",id)
			list_id.append(id)
		#
			list_id = list(set(list_id))
		return list_id
	except Exception as e:
		print("出错了get_product_id_list==",e)
		return None
if __name__ == "__main__":
	main()
	cursor.close()
	conn.close()
	# print(get_product_id_list("胸罩"))
