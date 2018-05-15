from urllib import parse
from urllib.request import Request,urlopen


#保存下载好的页面
def save(data,num):

	with open("第"+str(num)+"页.html","wb") as f:
		f.write(data)

	print("第"+str(num)+"页保存完毕!")

#请求网页
def page_download(newurl,num):
	headers = {
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"

	}
	request = Request(newurl,headers=headers)

	reponse = urlopen(request)
	data = reponse.read()#
	print(data)
	save(data,num)


#拼接对应贴吧的页码
def baidu_spider(url,startpage,endpage):
	#https://tieba.baidu.com/f?kw=%E5%B0%9A%E7%A1%85%E8%B0%B7
	for num in range(startpage,endpage+1):
		print(num)
		# n代表页数,m每页多少条数据;分页的公式: (n-1)*m,m
		pn = (num-1)*50
		newurl = url +"&ie=utf-8&pn="+str(pn)
		print("newurl==",newurl)
		page_download(newurl,num)


def main():
	kw = input("请输入您要抓取贴吧的名称:")
	startpage = int(input("请输入要抓取的起始页面:"))
	endpage = int(input("请输入抓取的结束页:"))


	kw = {"kw":kw}
	#url编码
	kw = parse.urlencode(kw)

	#拼接url
	url = "https://tieba.baidu.com/f?"+kw
	print(url)

	#把url和要请求的页
	baidu_spider(url,startpage,endpage)



if __name__ == "__main__":
	main()