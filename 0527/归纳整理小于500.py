import sqlalchemy
import pandas
import matplotlib.pyplot as pl

def main():
    conn = sqlalchemy.create_engine('sqlite:///bra.sqlite')
    sql = "select size1,size2 from sales;"
    df = pandas.read_sql(sql, conn)
    size1size2content = df.groupby(['size1', 'size2'])['size1'].count()
    # 总和
    size1size2sum = size1size2content.sum()
    # 转换成dataframe
    size1size2 = size1size2content.to_frame(name='销量')

    # 销量小于或者等于500的数据归纳为其他
    n = 500
    other_data = size1size2[size1size2['销量'] <= n].sum()
    # 创建一个其他
    other = pandas.DataFrame([other_data], index=pandas.MultiIndex(levels=[[''], ['其他']], labels=[[0], [0]]))


    size1size2 = size1size2[size1size2['销量'] > n].append(other)


    # 插入比例
    pandas.options.display.float_format = '{:,.2f}%'.format
    size1size2.insert(0, '比例', 100.0*size1size2content/size1size2sum)
    # 排序按照销量降序
    size1size2 = size1size2.sort_values(['销量'], ascending=[0])
    table1 = size1size2.index.tolist()

    table1_new = []
    for lable in table1:
        table1_new.append(lable[1]+lable[0])

    pl.pie(size1size2['销量'], labels=table1_new, autopct='%.2f%%')
    pl.axis('equal')
    pl.title('罩杯+下胸杯综合分析')
    pl.legend(loc='upper left')
    pl.show()
if __name__ == '__main__':
    main()