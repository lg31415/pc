# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from tx.items import TencentItem


class TengxunpoSpider(CrawlSpider):
    name = 'tengxunpo'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['https://hr.tencent.com/position.php?&start=0#a']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = TencentItem()

        all_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')

        for postion in all_list:
            position_name = postion.xpath("./td[1]/a/text()").get()
            position_link = postion.xpath("./td[1]/a/@href").get()
            position_type = postion.xpath("./td[2]/text()").get()
            people_num = postion.xpath("./td[3]/text()").get()
            work_address = postion.xpath("./td[4]/text()").get()
            publish_time = postion.xpath("./td[5]/text()").get()
            item["position_name"] = position_name
            item["position_link"] = position_link
            item["position_type"] = position_type
            item["people_num"] = people_num
            item["work_address"] = work_address
            item["publish_time"] = publish_time
            yield item
