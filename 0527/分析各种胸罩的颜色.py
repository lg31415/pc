import sqlalchemy
import pandas
import matplotlib.pyplot as pl
from matplotlib.pyplot import subplots

def main():
    conn = sqlalchemy.create_engine('sqlite:///bra.sqlite')
    df = pandas.read_sql('select color from sales', conn)

    # 按照颜色分组
    colorcount = df.groupby('color')['color'].count()

    # 总数
    colortotal = colorcount.sum()

    # 转换类型
    colorsize = colorcount.to_frame(name='销量')

    # 把小于或者等于1000的归为其他
    n = 1000
    other = colorsize[colorsize['销量'] <= n].sum()
    other_data = pandas.DataFrame([other], index=pandas.MultiIndex(levels= [['其他']],labels=[[0]]))
    colorsize = colorsize[colorsize['销量'] > n].append(other_data)

    # 插入比例
    pandas.options.display.float_format = '{:,.2f}%'.format
    colorsize.insert(0, '比例', 100.0*colorcount/colortotal)
    # 排序
    colorsize = colorsize.sort_values(['销量'], ascending=False)
    lable1 = colorsize.index.tolist()
    # 设置突出显示
    explode = (0, 0, 0, 0.1, 0, 0, 0)
    pl.pie(colorsize['销量'], labels=lable1, autopct='%.2f%%',explode=explode)
    pl.legend(loc=2)
    pl.axis('equal')
    pl.title('罩杯颜色统计')
    pl.show()


if __name__ == '__main__':
    main()