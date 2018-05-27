import sqlalchemy
import pandas
from matplotlib.pyplot import show,subplots

def main():
    sql = sqlalchemy.create_engine('sqlite:///bra.sqlite')
    cotent = "select * from sales"
    ac = pandas.read_sql(cotent, sql)
    # 天猫的每个销量
    tianmaSize = ac[ac['source'] == "天猫"].groupby("size1")['size1'].count()
    tianmaosum = tianmaSize.sum()
    #转换类型
    tianmaosize1 = tianmaSize.to_frame(name="销量")
    # 插入比例
    pandas.options.display.float_format = "{:,.2f}%".format
    tianmaosize1.insert(0, '比例', 100.0*tianmaSize/tianmaosum)
    # 修改索引
    tianmaosize1.index.names = ['胸罩']
    print(tianmaosum)
    # 京东的每个销量
    jingdongSize = ac[ac['source'] == "京东"].groupby("size1")['size1'].count()
    jingdongsum = jingdongSize.sum()
    jingdongsize1 = jingdongSize.to_frame(name='销量')
    # 插入比例
    jingdongsize1.insert(0, '比例', 100.0*jingdongSize/jingdongsum)
    # 修改索引
    jingdongsize1.index.names = ['胸罩']
    get_mu(tianmaosize1, jingdongsize1)

def get_mu(tianmaosize1,jingdongsize1):
    tianmao = []
    jingdong = []
    tianmao = tianmaosize1.index.tolist()
    jingdong = jingdongsize1.index.tolist()
    for i in range(len(tianmao)):
        tianmao[i] = tianmao[i] + "胸罩"

    for a in range(len(jingdong)):
        jingdong[a] = jingdong[a] + "胸罩"

    gig,(ax1,ax2) = subplots(1, 2, figsize=(14, 6))

    ax1.pie(jingdongsize1["销量"], labels=jingdong, autopct='%.2f%%')
    ax2.pie(tianmaosize1['销量'], labels=tianmao, autopct='%.2f%%')

    ax1.legend()
    ax2.legend()

    ax1.axis('equal')
    ax2.axis('equal')

    show()
if __name__ == '__main__':
    main()