# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings


class LelivePipeline(object):
    def open_spider(self, spider):
        print('开始')

    def __init__(self):
        self.file = open('乐视直播.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        dict_item = dict(item)
        json_text = json.dumps(dict_item,ensure_ascii=False) + '\n'
        self.file.write(json_text)
        return item

    def close_spider(self, spider):
        print('over')
        self.file.close()


# 保存图片的
class LelivesaveImage(ImagesPipeline):
    # 得到图片的配置路径
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    # 请求图片
    def get_media_requests(self, item, info):
        # 图片存放的路径
        image_path = item['image_link']
        # 把图片交给引擎
        yield scrapy.Request(image_path)

    def item_completed(self, results, item, info):
        # image_path = [x['path'] for ok, x in results if ok]
        for ok, x in results:
            if ok:
                image_path = x['path']
        old_image_name = self.IMAGES_STORE+'/'+image_path[0]
        new_image_name = self.IMAGES_STORE+'/'+item['nick_name'] + '.jpg'

        os.rename(old_image_name,new_image_name)

        # 新的字典
        item['image_path'] = new_image_name
        return item