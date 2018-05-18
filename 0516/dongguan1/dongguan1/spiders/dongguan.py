# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from dongguan1.items import Dongguan1Item


class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']
    offset = 0
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page=' + str(offset)
    start_urls = [url]

    rules = (
        Rule(LinkExtractor(allow=r'type=4')),
        Rule(LinkExtractor(allow=r'question/\d+/\d+.shtml'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = Dongguan1Item()
        # 帖子的链接
        url = response.url
        # 帖子标题
        tieles = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        title = tieles.split('\xa0\xa0')[0].split('：')[1]
        # 帖子编号
        num = tieles.split('\xa0\xa0')[1].split(':')[1]
        # 帖子内容
        content = response.xpath('//div[@class="pagecenter p3"]//div[@class="c1 text14_2"]/text()').extract()
        if len(content) == 0:
            content = response.xpath('//div[@class="pagecenter p3"]//div[@class="contentext"]/text()').extract()
            content = ''.join(content)
        else:
            content = ''.join(content)

        item['ac_title'] = title
        item['ac_link'] = url
        item['ac_content'] = content
        item['ac_number'] = num
        yield item
