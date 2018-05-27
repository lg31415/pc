# -*- coding: utf-8 -*-
import scrapy
from meizi.items import MeiziItem

class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    allowed_domains = ['meizitu.com']
    page = 1
    url = 'http://www.meizitu.com/a/more_'
    start_urls = [url+str(page)+'.html']

    def parse(self, response):
        link_list = response.xpath('//div[@class="inWrap"]/ul[@class="wp-list clearfix"]/li[@class="wp-item"]//a/@href').extract()
        for link in link_list:
            print(link)
            yield scrapy.Request(link, callback=self.meizi_link)

    def meizi_link(self,response):
        title = response.xpath('//div[@class="metaRight"]/h2/a/text()').extract()
        images = response.xpath('//div[@class="postContent"]/div[@id="picture"]/p/img/@src').extract()

        for image in images:
            item = MeiziItem()
            item['titles'] = title
            item['image'] = image
            item['url'] = response.url
            yield item