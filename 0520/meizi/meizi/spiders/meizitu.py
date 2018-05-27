# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.loader import ItemLoader,Identity
from meizi.items import MeiziItem


class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    allowed_domains = ['meizitu.com']
    url = 'http://www.meizitu.com/'
    start_urls = [url]

    def parse(self, response):
       link_list = response.xpath('//h2/a/@href').extract()
       for link in link_list:
           yield scrapy.Request(link, callback=self.parse_item)


    def parse_item(self, response):
        item_loader = ItemLoader(item=MeiziItem(), response=response)

        # 标题
        item_loader.add_xpath('title', '//h2/a/text()')
        # 图片链接
        item_loader.add_xpath('image', "//div[@id='picture']/p/img/@src", Identity())
        # 帖子链接
        item_loader.add_xpath('link', response.url)

        return item_loader.load_item()