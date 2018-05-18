# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AcfunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 作者昵称
    names = scrapy.Field()
    # 播放主题
    titles = scrapy.Field()
    # 发布时间
    times = scrapy.Field()
    # 视频连接
    video_link = scrapy.Field()
    # 作者空间
    homeb = scrapy.Field()
    # 播放次数
    numbers = scrapy.Field()