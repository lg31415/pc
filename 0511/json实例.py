import json

#python对象
list_str=[1,2,3,4]
#把Python对象装换为json对象
str_list = json.dumps(list_str)
print(type(str_list))

