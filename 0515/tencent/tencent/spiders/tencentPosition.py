# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['hr.tencent.com']
    page_nums = 0
    url = 'https://hr.tencent.com/position.php?&start='
    start_urls = [url + str(page_nums) + '#a']

    def parse(self, response):
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

        if self.page_nums < int(response.xpath('//tr[@class="f"]/td/div/span/text()').get()):
            self.page_nums += 10
        url = self.url + str(self.page_nums) +'#a'
        yield scrapy.Request(url, callback=self.parse)