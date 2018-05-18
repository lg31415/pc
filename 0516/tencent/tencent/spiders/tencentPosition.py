# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tencent.items import TencentItem


class TencentpositionSpider(CrawlSpider):
    name = 'tencentPosition'
    # allowed_domains = ['s2.lulujjs.club']
    start_urls = [
        'http://s2.lulujjs.club/pw/thread.php?fid=3&page=1',
        'http://1024.hlork9.org/pw/thread.php?fid=3&page=1',
        'http://d2.sku117.org/pw/thread.php?fid=3&page=1'
    ]

    rules = (
        Rule(LinkExtractor(allow=r'fid=3')),
        Rule(LinkExtractor(allow=r'page=\d+'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):

        item = TencentItem()
        # #content = response.text
        # #bodys = response.xpath('//tbody')
        name = response.xpath('//tr/td/h3/a/text()').extract()
        if len(name) == 0:
            pass
        else:
            for i in name:
                i = ''.join(i)
                item['article_name'] = i
        link = response.xpath('//tr/td/h3/a/@href').extract()
        if len(link) == 0:
            pass
        else:
            for l in link:
                l = ''.join(l)
                item['article_link'] = 'http://d2.sku117.org/pw/' + l
        yield item
