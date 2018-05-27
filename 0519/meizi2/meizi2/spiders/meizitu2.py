# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.loader import ItemLoader,Identity



class Meizitu2Spider(scrapy.Spider):
    name = 'meizitu2'
    allowed_domains = ['meizitu.com']
    page = 1
    url = 'http://www.meizitu.com/a/more_'
    start_urls = [url+str(page)+'.html']

    def parse(self, response):
        title = response.xpath('//div[@class="metaRight"]/h2/a/text()').extract()
        images = response.xpath('//div[@class="postContent"]/div[@id="picture"]/p/img/@src').extract()
        for image in images:
            item = MeiziItem()
            item['titles'] = title
            item['image'] = image
            item['url'] = response.url
            yield item