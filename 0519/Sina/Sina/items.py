# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 父标题
    parent_title = scrapy.Field()
    # 父链接
    parent_url = scrapy.Field()
    # 子标题
    son_title = scrapy.Field()
    # 子链接
    son_url = scrapy.Field()

    # 新闻+国内
    parent_path = scrapy.Field()

    # 帖子了标题
    grandson_title = scrapy.Field()
    # 帖子的link
    grandson_url = scrapy.Field()
    # 帖子的内容
    grandson_content = scrapy.Field()
