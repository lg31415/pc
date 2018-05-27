import pandas
import matplotlib.pyplot as plot

df = pandas.read_csv("gapminder.tsv", sep='\t')

#全球平均寿命
global_yearly_file = df.groupby("year")["lifeExp"].mean()

print(global_yearly_file)

# 使用matplotlib可视化显示一维表数据
global_yearly_file.plot()
# 显示士例
plot.legend()
# 显示标题
plot.title("全球平均寿命")
# 显示
plot.show()