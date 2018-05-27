import pymongo
import redis
import json


def main():
    # 端口不要加双引号
    mgclient = pymongo.MongoClient(host="localhost", port=27017)
    reclient = redis.StrictRedis(host="192.168.1.18", port=6379, db=0)
    # 创建数据库
    sinadb = mgclient['sinadb']
    # 创建表
    sheetname = sinadb['sina_items']
    i = 1

    while True:
        # 从Redis数据去
        # 先进先出
        source, data = reclient.blpop('sinaspider_redis:items')
        print('=====', source)
        # 把bytes类型转换成Python字典类型
        item = json.loads(data.decode('utf-8'), encoding='utf-8')
        print('------>', item)

        # 把数据家居存入MongoDB数据库
        sheetname.insert(item)
        print('i======>', i)
        i += 1


if __name__ == '__main__':
    main()
