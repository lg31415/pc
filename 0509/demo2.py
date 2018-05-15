import re
content = 'hello world python and python atguigu!'

pattern = re.compile(r'python')

tet = pattern.match(content,len('hello world '),len(content))
print(tet)
print(tet.group())