# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class TxPipeline(object):
    def open_spider(self, spider):
        print('开始时调用')

    def __init__(self):
        self.file = open('腾讯.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        dict_item = dict(item)
        text = json.dumps(dict_item, ensure_ascii=False) + '\n'
        self.file.write(text)
        return item

    def close_spider(self, spider):
        print('over')
        self.file.close()