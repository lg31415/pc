# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class SinaPipeline(object):
    def open_spider(self, spider):
        self.file = open('sina.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        python_item = dict(item)
        python_text = json.dumps(python_item, ensure_ascii=False)
        self.file.write(python_text)
        return item

    def close_spider(self, spider):
        self.file.close()


class SinaContentPipeline(object):
    def prosess_item(self, item, spider):
        python_dic = dict(item)
        parent_path = item['parent_path']
        sun_content = item['grandson_content']
        sun_url = item['grandson_url']
        new_f_name = parent_path + '/' + sun_url[7:sun_url.rfind(".")].replace('/', '_') + 'txt'

        with open(new_f_name, 'w', encoding='utf-8') as f:
            f.write(sun_content)
        return item
