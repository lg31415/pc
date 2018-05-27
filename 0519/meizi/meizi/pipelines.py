# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from meizi.settings import IMAGES_STORE
import os


class MeiziPipeline(object):
    def process_item(self, item, spider):
        return item


class MeiziImageipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image = item['image']
        yield scrapy.Request(image)

    def item_completed(self, results, item, info):
        image = [x['path'] for ok, x in results if ok][0]
        old_name = IMAGES_STORE + '/' + image
        new_name = IMAGES_STORE + '/' + item['image'][7:].replace('/', '_')
        os.rename(old_name, new_name)
        item['image_path'] = new_name
        return item
