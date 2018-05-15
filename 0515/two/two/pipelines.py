# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
# 存储数据musql mogangdb,redis 
class TwoPipeline(object):
    def open_spid(self,spider):
        print("爬虫开始经过")

    def __init__(self):
        # 创建保存的文件
        # w 代表这一次爬虫写入
        self.file = open("atguigu_theacher.json", "w", encoding="utf-8")

    # 处理每条数据
    def process_item(self, item, spider):
        # 转换为utf-8类型
        item_dict = dict(item)
        # 第一个参数是Python的字典对象
        json_text = json.dumps(item_dict,ensure_ascii=False)+"\n"
        self.file.write(json_text)
        return item

    def close_spid(self,spider):
        # 当爬虫结束的时候调用
        self.file.close()