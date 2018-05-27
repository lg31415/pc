import sqlalchemy
import pandas
import matplotlib.pyplot as pl
from matplotlib.font_manager import FontProperties
font = FontProperties(fname="/Library/Fonts/Songti.ttc")


# 创建引擎
sql = sqlalchemy.create_engine("sqlite:///bra_all.sqlite")

# 查询语句
content = "select source, size1 from sql_tm"

# 返回一个datafarme类型
df = pandas.read_sql(content,sql)

# 统计各组的销量
size1nums = df.groupby("size1")["size1"].count()

# 求出享受总量
size1_nums = size1nums.sum()

# 转换成dataframe类型
size = size1nums.to_frame(name="销量")

# 插入比例
scal = 100.0*size1nums/size1_nums
pandas.options.display.float_format = "{:,.2f}%".format
size.insert(0, "比例", scal)
# 修改索引
size.index.names = ['罩杯']
biaoqian = ['A罩杯', 'B罩杯', 'C罩杯','D罩杯']
liebiao = ['A', 'B', 'C','D']
count = size['销量']
# 绘制数据
pl.pie(count, autopct="%0.2f%%", labels=biaoqian)
# 使圆均匀显示
pl.axis("equal")
# 设置图的标题并设置字体
pl.title("胸罩销量", FontProperties=font)
# 显示示例
pl.legend(liebiao)
pl.show()