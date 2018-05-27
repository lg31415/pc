# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeiziItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 帖子标题
    titles = scrapy.Field()
    # 帖子对应图片链接
    image = scrapy.Field()
    # 帖子链接
    url  = scrapy.Field()
    # 图片保存多个路径
    image_path = scrapy.Field()
