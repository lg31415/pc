# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class TopSpider(scrapy.Spider):
    name = 'top'
    allowed_domains = ['douban.com']
    offset = 0
    urls = 'https://movie.douban.com/top250?start='+str(offset)+'&filter='
    start_urls = [urls]

    def parse(self, response):
        item = DoubanItem()
        moves = response.xpath('//div[@class="info"]')
        for move in moves:

            name = move.xpath('.//span[@class="title"][1]/text()').extract()[0]
            item['video_name'] = name
            contents = move.xpath('.//div[@class="bd"]/p[1]/text()').extract()[0]
            item['content'] = contents
            num = move.xpath('.//div[@class="star"]/span[2]/text()').extract()[0]
            item['numbers'] = num
            intro1 = move.xpath('.//span[@class="inq"]/text()').extract()
            if len(intro1) > 0:
                intro1 = intro1[0]

            item['intro'] = intro1

            yield item


        if self.offset < 225:
            self.offset += 25
        url = 'https://movie.douban.com/top250?start='+str(self.offset)+'&filter='
        yield scrapy.Request(url, callback=self.parse)