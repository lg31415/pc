import re
from bs4 import BeautifulSoup
from urllib3 import PoolManager,disable_warnings

disable_warnings()

def main():
	url='https://list.tmall.com/search_product.htm?q=%D0%D8%D5%D6&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&xl=xio_6&from=mallfp..pc_1_suggest&smToken=5abff42f85364330a9d348d75771021d&smSign=4FVAKGk34VDHat2XRo97Wg%3D%3D'
	headers = {
		"authority": "list.tmall.com",
		"method": "GET",
		"path": "/search_product.htm?q=%E6%8C%AF%E5%8A%A8%E6%A3%92&imgfile=&commend=all&ssid=s5-e&search_type=tmall&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306",
		"scheme": "https",
		"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "zh,zh-CN;q=0.9,en;q=0.8,zh-HK;q=0.7,zh-TW;q=0.6",
		"cache-control": "max-age=0",
		"cookie": "cna=AjF3EzXpoHwCAXlFUaa/Y3JS; _m_h5_tk=ced869e971b45a9df4298fc5a711344d_1526020994805; _m_h5_tk_enc=ceef7ffdf83ef4b874cbc6c86393867d; tk_trace=1; t=8f304c8602dd7313b7cdd553df7daeae; _tb_token_=76ee36bb6dfed; cookie2=1c7e8f7e65adac30811c13574172e19b; _med=dw:800&dh:450&pw:1600&ph:900&ist:0; dnk=tb38177906; uc1=cookie14=UoTeOLn7%2Bx0z1Q%3D%3D&lng=zh_CN&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&existShop=true&cookie21=UIHiLt3xTIkz&tag=10&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&pas=0; uc3=nk2=F5RGPuOuWloe5w%3D%3D&id2=UoH4F%2BdP0cvWcw%3D%3D&vt3=F8dBz44hYvtIyKsBqjg%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=tb38177906; lid=tb38177906; _l_g_=Ug%3D%3D; unb=1072232399; lgc=tb38177906; cookie1=BqJl%2B4QQg2D2Egwr2%2FKxhHqky%2BijJOjtwvIikmPJvoA%3D; login=true; cookie17=UoH4F%2BdP0cvWcw%3D%3D; _nk_=tb38177906; sg=692; csg=823d533c; enc=h847uHTNZOwQCMeIRYQHYo2rqS9iC13zf%2Fu1ZIcDwJp6rU86VPcreLy3ajw8iXv3GWdwdmYnLMKtiz0wn7fdNw%3D%3D; tt=taobao-main; res=scroll%3A1170*6574-client%3A1170*365-offset%3A1170*6574-screen%3A1600*900; pnm_cku822=098%23E1hvKpvUvbpvUpCkvvvvvjiPPFdvsjYURLz96jrCPmPWgjYRR2Mhsj1WnLM9ljtjRpGCvvpvvPMMKphv8vvvvUrvpv2qvvvmoZCvCbZvvvW9phvWh9vvvgivpvAlvvvmoZCv2b7ivpvUvvmv%2BpqW3OeEvpvVmvvC9cXvmphvLvBNgpvj7iLp%2BE7reC69D7zZaB4AVArlYWoQrEt6pa2v%2BnezrmphQRAn3feAOHcIAXcBKFyK2ixr1RoKD7rjiNLh1E9faHFXS47BhC9CvpvVvmvvvhCvRphvCvvvvvm5vpvhvvmv99%3D%3D; cq=ccp%3D0; isg=BAMDdT6RXZ-3IxFrFwvy5ta6ksFt0IKeRBVzJTXgXWLZ9CMWvUgnCuHFaoy6z--y",
		"referer": "https://www.taobao.com/?spm=a1z02.1.1581860521.1.2e34782dcGrYnY",
		"upgrade-insecure-requests": "1",
		"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36",
	}
	http = PoolManager()
	html = http.request("GET",url=url,headers=headers)
	result = html.data.decode('GB18030')
	print(result)
	soup = BeautifulSoup(result,'lxml')
	cont = soup.find_all(href=re.compile(r'//detail.tmall.com/item.htm'))
	print(cont)
	for i in cont:
		print(i['href'])


if __name__ == '__main__':
	main()