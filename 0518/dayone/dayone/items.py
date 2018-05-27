# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DayoneItem(scrapy.Item):
    # 获取帖子标题
    title = scrapy.Field()
    # 获取帖子编号
    numbers = scrapy.Field()
    content = scrapy.Field()