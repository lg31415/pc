import json
#json数据
str_list = "[1,2,3,4]"
str_dict = '{"name":"张三","age":18}'
print(str_list)
print(str_dict)


#转化Python对象
str_dict1 = json.loads(str_dict)
print(str_dict1)