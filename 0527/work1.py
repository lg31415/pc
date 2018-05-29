import sqlalchemy
import pandas
from matplotlib.pyplot import show,subplots

def main():
    conn = sqlalchemy.create_engine('sqlite:///bra.sqlite')
    df = pandas.read_sql('select * from sales', conn)
    tianmao = df[df['source'] == '天猫'].groupby('size2')['size2'].count()
    jingdong = df[df['source'] == '京东'].groupby('size2')['size2'].count()

    # 总数
    tianmaototal = tianmao.sum()
    jingdongtotal = jingdong.sum()
    # 类型
    tianmaosize = tianmao.to_frame(name='销量')
    jingdongsize = jingdong.to_frame(name='销量')
    # 插入比例

    pandas.options.display.float_format = "{:,.2f}%".format
    tianmaosize.insert(0, '比例', 100.0*tianmao/tianmaototal)
    jingdongsize.insert(0, '比例', 100.0*jingdong/jingdongtotal)
    print(jingdongsize)

    # 显示
    table1 = []
    table2 = []
    table1 = tianmaosize.index.tolist()
    table2 = jingdongsize.index.tolist()

    for i in range(len(table1)):
        table1[i] = table1[i]

    for a in range(len(table2)):
        table2[a] = table2[a]

    gig, (ax1,ax2) = subplots(1, 2, figsize=(14, 8))
    ax1.pie(tianmaosize['销量'], labels=table1, autopct='%.2f%%')
    ax2.pie(jingdongsize['销量'], labels=table2, autopct='%.2f%%')
    ax1.axis('equal')
    ax2.axis('equal')
    ax1.legend()
    ax2.legend()
    ax1.set_title('天猫胸罩销量')
    ax2.set_title('京东胸罩销量')
    show()

if __name__ == '__main__':
    main()