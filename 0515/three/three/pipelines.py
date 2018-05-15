# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class ThreePipeline(object):
    def open_spid(self):
        print("开始调用")

    def __init__(self):
        self.file = open("teacher.json", "w", encoding="utf-8")

    def process_item(self, item, spider):
        dict_item = dict(item)
        f_text = json.dumps(dict_item, ensure_ascii=False) + "\n"
        self.file.write(f_text)
        return item

    def close_spid(self):
        print("结束调用！")
