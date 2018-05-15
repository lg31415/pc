import requests
import json
import jsonpath
url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/65.0.3325.146 Safari/537.36"}
response = requests.get(url,headers=headers)
html = response.text
#转换为Python对象
py_dict = json.loads(html,encoding="utf-8")


py_list = jsonpath.jsonpath(py_dict,"$..name")

f = open("city.txt","w",encoding="utf-8")

json.dump(py_list,f,ensure_ascii=False)
print("over!you sussccy!")