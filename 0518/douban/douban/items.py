# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 电影名称
    video_name = scrapy.Field()
    # 电影主演信息
    content = scrapy.Field()
    # 电影屏风
    numbers = scrapy.Field()
    # 电影简介
    intro = scrapy.Field()
