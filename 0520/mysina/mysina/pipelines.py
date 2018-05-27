# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime


class MysinaPipeline(object):
    def process_item(self, item, spider):
        small_son_link = item['small_son_link']
        small_path = item['small_path']
        content = item['ac_content']
        file = small_son_link[7:small_son_link.rfind('.')].replace('/', '_') + '.txt'
        with open(small_path + '/' + file, 'w', encoding='utf-8') as f:
            f.write(content)
        return item

class ExamplePipeline(object):
    def process_item(self, item, spider):
        item['crawled'] = datetime.datetime.utcnow()
        item['spider'] = spider.name

        return item
