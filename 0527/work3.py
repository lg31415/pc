# 罩杯与下胸围总和分析
import pandas
import sqlalchemy
import matplotlib.pyplot as pl

def main():
    conn = sqlalchemy.create_engine('sqlite:///bra.sqlite')
    df = pandas.read_sql('select color from sales',conn)
    size1size2count = df.groupby('color')['color'].count()
    # 总和
    size1size2total = size1size2count.sum()
    # 转换类型
    size = size1size2count.to_frame(name='销量')

    # 插入其他
    n = 1000
    other_data = size[size['销量'] <= n].sum()
    other = pandas.DataFrame([other_data], index=pandas.MultiIndex(levels=[['其他']], labels=[[0]]))
    size = size[size['销量'] > n].append(other)

    # 插入比例
    pandas.options.display.float_format = '{:,.2f}%'.format
    size.insert(0, '比例', 100.0*size1size2count/size1size2total)

    table = size.index.tolist()
    # 显示
    explode = (0, 0, 0.1, 0.1, 0, 0, 0)
    pl.pie(size['销量'], labels=table, autopct='%.2f%%', explode=explode)
    pl.axis('equal')
    pl.legend(loc=4)
    pl.title('颜色')
    pl.show()

if __name__ == '__main__':
    main()