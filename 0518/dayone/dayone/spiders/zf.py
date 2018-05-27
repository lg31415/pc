# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from dayone.items import DayoneItem


class ZfSpider(CrawlSpider):
    name = 'zf'
    allowed_domains = ['wa.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        Rule(LinkExtractor(allow=r'page=\d')),
        Rule(LinkExtractor(allow=r'/question/\d+/\d+.shtml'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        try:
            item = DayoneItem()
            url = response.url
            titles = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
            # 帖子的标题 
            title1 = titles.split("\xa0\xa0")[0].split("：")[1]
            # 帖子的编号 
            number = titles.split("\xa0\xa0")[1].split(":")[1]

            content2 = response.xpath('//div[@class="c1 text14_2"]/text()|//div[@class="contentext"]/text()').extract()
            content1 = "".join(content2)
            item['name'] = title1
            item['numbers'] = number
            item['content'] = content1
            yield item
        except Exception as e:
            print(e)
