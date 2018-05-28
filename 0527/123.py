import sqlalchemy
import pandas
from matplotlib.pyplot import subplots,show

def main():
    tianmao = sqlalchemy.create_engine('sqlite:///bra.sqlite')

    jingdong = sqlalchemy.create_engine('sqlite:///bra.sqlite')

    # 天猫的数据
    sql = 'select * from main.sales'
    df = pandas.read_sql(sql, tianmao)
    tianmao_zu = df[df['source'] == '天猫'].groupby('size1')['size1'].count()
    tianmao_sums = tianmao_zu.sum()
    # 类型转换
    tianmao_size = tianmao_zu.to_frame(name='销量')
    # 插入比例
    pandas.options.display.float_format = '{:,.2f}%'.format
    tianmao_size.insert(0, '比例', 100.0*tianmao_zu/tianmao_sums)
    # 京东数据
    jingdong_zu = df[df['source'] == '京东'].groupby('size1')['size1'].count()
    jingdong_sums = jingdong_zu.sum()
    # 类型转换
    jingdong_size = jingdong_zu.to_frame(name='销量')
    # 插入比例
    pandas.options.display.float_format = '{:,.2f}%'.format
    jingdong_size.insert(0, '比例', 100.0*jingdong_zu/jingdong_sums)
    print(jingdong_size)
    get_tuxing(tianmao_size, jingdong_size)

def get_tuxing(tiaomao_size, jingdong_size):
    table1 = []
    table2 = []
    table1 = tiaomao_size.index.tolist()
    table2 = jingdong_size.index.tolist()

    for i in range(len(table1)):
        table1[i] = table1[i] + '胸罩'

    for a in range(len(table2)):
        table2[a] = table2[a] + '胸罩'

    gig, (ax1, ax2) = subplots(1, 2, figsize=(14, 6))
    ax1.pie(jingdong_size["销量"], labels=table1, autopct='%.2f%%')
    ax2.pie(tiaomao_size['销量'], labels=table2, autopct='%.2f%%')
    ax1.axis('equal')
    ax2.axis("equal")

    show()

if __name__ == '__main__':
    main()