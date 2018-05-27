# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MysinaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 大标题与连接
    big_title = scrapy.Field()
    big_link = scrapy.Field()

    # 小标题与连接
    small_title = scrapy.Field()
    small_link = scrapy.Field()

    # 小标题的儿子的存储路径
    small_path = scrapy.Field()
    # 小标题的链接
    small_son_link = scrapy.Field()
    # 文章的标题与内容
    ac_title = scrapy.Field()
    ac_content = scrapy.Field()

    # 增加爬虫的名称和时间戳 
    crawled = scrapy.Field()
    spider = scrapy.Field()
