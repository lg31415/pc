# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.utils.project import get_project_settings
import pymongo


# 保存到MongoDB数据库,格式是字典插入
class DoubanMongodbPipeline(object):
    def __init__(self):
        host = get_project_settings().get('MONGODB_HOST')
        port = get_project_settings().get('MONGODB_PORT')
        dbname = get_project_settings().get('MONGODB_DBNAME')
        sheetname = get_project_settings().get('MONGODB_SHEETNAME')
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client['dbname']
        self.port = mydb['sheetname']

    def process_item(self, item, spider):
        dict_item = dict(item)
        # 插入数据库
        self.port.insert(dict_item)
        return item


# 保存到本地json格式
class DoubanPipeline(object):
    def open_spider(self, spider):
        self.file = open('douban.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        dict_item = dict(item)
        a = json.dumps(dict_item, ensure_ascii=False) + '\n'
        self.file.write(a)
        return item

    def close_spider(self, spider):
        self.file.close()
