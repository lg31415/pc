import sqlalchemy
import pandas
import matplotlib.pylab as plb
from matplotlib.font_manager import FontProperties
font = FontProperties(fname='/Library/Fonts/Songti.ttc')
# 打开数据库文件,创建引擎可以操作数据
sql = sqlalchemy.create_engine("sqlite:///bra_all.sqlite")
# sql语句
content = "select source,size1 from sql_tm"
# 使用pandas的read_sql函数，查询数据库中的source字典数据，返回的是id字段，并且返回类型是dataframe（pandas中的一种数据类型）
df = pandas.read_sql(content, sql)

size1Count = df.groupby("size1")["size1"].count() # 统计各组的销量
# print(size1Count)
# Series类型
# print(type(size1Count))
# 各组销量的总计之和
sizeTotal = size1Count.sum()
# 吧series转换为dataFrame类型
size1 = size1Count.to_frame(name="销量")
# print(size)
# print(type(size))
# 插入比例
scal = 100.0*size1Count/sizeTotal
# print(scal)
# 设置格式化输出
pandas.options.display.float_format = "{:,.2f}%".format

# 插入比例
size1.insert(0,"比例", scal)
# 修改索引名称
size1.index.names = ['罩杯']
# 打印结果
print(size1)
# 设置标签
lables1 = ["A","B","C"]
lables2 = ["A","B","C"]
sales_num = size1['销量']
# 绘制病状第一个参数是数据，第二个参数是数据的一个格式化，第三个参数是标签
plb.pie(sales_num,autopct="%.2f%%", labels=lables1)
# 设置圆形并且均匀
plb.axis('equal')
# 设置图的标题
plb.title("罩杯销售量",FontProperties=font)
# 设置示例
plb.legend(lables2)
plb.show()