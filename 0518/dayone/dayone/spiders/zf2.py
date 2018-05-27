# -*- coding: utf-8 -*-
import scrapy

from dayone.items import DayoneItem


class Zf2Spider(scrapy.Spider):
    name = 'zf2'
    allowed_domains = ['wz.sun0769.com']
    offset = 0
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    start_urls = [url + str(offset)]

    def parse(self, response):
        urls = response.url

        tz_link = response.xpath('//a[contains(@href,"/html/question/")]/@href').extract()
        for l in tz_link:
            yield scrapy.Request(l, callback=self.parse_item)

        if self.offset < 80000:
            self.offset += 30
            url = self.url+str(self.offset)
            yield scrapy.Request(url, callback=self.parse)

    def parse_item(self, response):
        item = DayoneItem()
        url = response.url
        titles = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        # 帖子的标题 
        title1 = titles.split("\xa0\xa0")[0].split("：")[1]
        # 帖子的编号 
        number = titles.split("\xa0\xa0")[1].split(":")[1]

        content2 = response.xpath('//div[@class="c1 text14_2"]/text()|//div[@class="contentext"]/text()').extract()
        if content2 == 0:
            content2 = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            content1 = "".join(content2)
        content1 = "".join(content2)
        item['title'] = title1
        item['numbers'] = number
        item['content'] = content1
        yield item