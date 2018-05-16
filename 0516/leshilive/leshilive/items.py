# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LeshiliveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #主播房间名字
    # 主播昵称
    nick_name = scrapy.Field()
    # 图片链接
    image_link = scrapy.Field()

    # 图片的保存路径
    image_path = scrapy.Field()
    # 房间链接
    data_link = scrapy.Field()

