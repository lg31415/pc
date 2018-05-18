# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class Dongguan1Pipeline(object):
    def open_spider(self, spider):
        self.flie = open('dg.json', 'a', encoding='utf-8')

    def process_item(self, item, spider):
        dict_item = dict(item)
        print('=='*50)
        self.flie.write('asdasdada')
        d_text = json.dumps(dict_item, ensure_ascii=False) + '\n'
        self.flie.write(d_text)
        return item

    def close_spider(self, spider):

        self.flie.close()
