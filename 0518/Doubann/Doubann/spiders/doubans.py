# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class DoubansSpider(CrawlSpider):
    name = 'doubans'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):

        content = response.xpath('//div[@class="article"]/ol[@class="grid_view"]').extract()
        for con in content:
            title = con.xpath('.//div[@class="hd"]/a/span[@class="title"][1]/text()').extract()
            print(title)