# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AtguiguItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 保存姓名
    name = scrapy.Field()

    # 保存简介
    info = scrapy.Field()

    # 保存老师图片
    image = scrapy.Field()