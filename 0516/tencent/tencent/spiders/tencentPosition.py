# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TencentpositionSpider(CrawlSpider):
    name = 'tencentPosition'
    # allowed_domains = ['s2.lulujjs.club']
    start_urls = [
         'http://s2.lulujjs.club/pw/thread.php?fid=3&page=1',
         'http://1024.hlork9.org/pw/thread.php?fid=3&page=1',
                  ]

    rules = (
        Rule(LinkExtractor(allow=r'page=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        print('aaaaaaaaa',response.url)
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
