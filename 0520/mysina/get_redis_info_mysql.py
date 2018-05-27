import  pymysql
import redis
import json

def main():
    reclient = redis.StrictRedis(host="192.168.1.18", port=6379, db=0)
    # 返回的是connectttions对象
    con = pymysql.connect(host='localhost', user='root', password='1234',
                          database='sinadb', port=3306, charset='utf8')

    # 通过con对象得到cursor对象
    cursor = con.cursor()

    i = 1
    while  True:
        # 从redis数据去
        # 先进先出
        source, data = rsclient.blpop(["sinaspider_redis:items"])
        # 把bytes类型转换成python字典类型
        item = json.loads(data.decode("utf-8"), encoding='utf-8')  # python字典
        args = [item['big_title'],item['big_link'],item['small_title'],item['small_link'],item['small_path'],item['small_son_link'],item['ac_title'],item['ac_content'],item['crawled'],item['spider']]
        sql = "INSERT INTO sina_items(big_title,big_link,small_title,small_link,small_path,small_son_link,ac_title,,ac_content,crawled,spider VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s))"
        # 把输几局存入MySQL
        cursor.execute(sql, args)
        # 事务提交
        con.commit()
        print('---->', i)
        i += 1

if __name__ == '__main__':
    main()