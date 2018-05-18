# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Dongguan1Item(scrapy.Item):
    # define the fields for your item here like:
    # 帖子标题
    ac_title = scrapy.Field()
    # 帖子链接
    ac_link = scrapy.Field()
    # 帖子内容
    ac_content = scrapy.Field()
    # 帖子编号
    ac_number = scrapy.Field()