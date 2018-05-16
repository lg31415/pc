# -*- coding: utf-8 -*-
import scrapy


class Dongguan2Spider(scrapy.Spider):
    name = 'dongguan2'
    allowed_domains = ['wz.sun0769.com']
    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset = 0
    start_urls = [url+str(offset)]

    def parse(self, response):
        # 所有帖子的链接
        text = response.url

        # 请求匹配的链接
        link = response.xpath('//a[contains(@href,"/html/question")]/@href').extract()

        for i in link():

            #帖子标题
            yield scrapy.Request(i,)



        if self.offset < 90750:
            self.offset += 30
            url = self.url+self.offset
            yield scrapy.Request(url,self.parse)
