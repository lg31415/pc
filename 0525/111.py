import sqlalchemy
import pandas
import matplotlib.pyplot as pl
from matplotlib.font_manager import FontProperties

font = FontProperties(fname='/Library/Fonts/Songti.ttc')

# 打开数据库的东西
sql = sqlalchemy.create_engine("sqlite:///bra_all.sqlite")
# 查询数据的操作
content = "select source,size1 from sql_tm"

# 进行查询
df = pandas.read_sql(content,sql)
# 每个罩杯的销售量
size1count = df.groupby("size1")["size1"].count()
# 销售总量
size1sum = size1count.sum()
# 转换为fram类型
size = size1count.to_frame("销量")

# 插入比例
scal = 100.0*size1count/size1sum
# 格式化输出
pandas.options.display.float_format = "{:,.2f}%".format
# 插入比例
size.insert(0, '比例', scal)
print(size)

size_num = size['销量']
pl.pie(size_num, autopct="%.2f%%")
pl.show()