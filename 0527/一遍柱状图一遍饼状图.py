import sqlalchemy
import pandas
import matplotlib.pyplot as pl
from matplotlib.pyplot import show,subplots

def main():
    # 创建引擎
    conn = sqlalchemy.create_engine('sqlite:///bra.sqlite')

    # 查询语句
    sql = "select * from sales"

    df = pandas.read_sql(sql, conn)

    tianmaocontent = df[df['source'] == '天猫'].groupby('size2')['size2'].count()
    jiongdongcontent = df[df['source'] == '京东'].groupby('size2')['size2'].count()
    # 类型转换
    size = tianmaocontent.to_frame(name='销量')
    # 总量
    sizesums = tianmaocontent.sum()
    # 插入索引
    pandas.options.display.float_format = '{:,.2f}%'.format
    size.insert(0, '比例', 100.0*tianmaocontent/sizesums)

    # 京东
    jingdongsum = jiongdongcontent.sum()
    jingdongsize = jiongdongcontent.to_frame('销量')
    # 插入索引
    pandas.options.display.float_format = '{:,.2f}%'.format
    jingdongsize.insert(0, '比例', 100.0*jiongdongcontent/jingdongsum)

    # 修改索引
    # size.index.names('大小')
    table1 = []
    table1Int = []
    table2 = []
    table1 = size.index.tolist()
    table2 = jingdongsize.index.tolist()
    for i in table1:
        table1Int.append(int(i))

    for a in range(len(table2)):
        table2[a] = table2[a] + '罩杯'

    gig,(ax1,ax2) = subplots(1, 2, figsize=(14, 8))
    ax1.bar(table1Int, size['销量'])
    ax2.pie(jingdongsize['销量'], labels=table2, autopct='%.2f%%')
    ax2.legend()
    ax1.set_title('天猫胸围比例')
    ax2.set_title('京东胸围比例')
    ax2.axis('equal')
    show()

if __name__ == '__main__':
    main()