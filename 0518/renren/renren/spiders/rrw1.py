# -*- coding: utf-8 -*-
import scrapy


class Rrw1Spider(scrapy.Spider):
    name = 'rrw1'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']


    def parse(self, response):

        scrapy.FormRequest.from_response(
            response,
            formdata={'email': 'yangguangfu2017@163.com', 'password': 'afu123456'},
            callback=self.log_sucess
        )

    def log_sucess(self,response):

        url = "http://www.renren.com/881820831/profile"
        yield scrapy.Request(url, callback=self.new_page)

    def new_page(self,response):
        url = response.url
        with open('zhengshuang.heml', 'w', encoding='utf-8') as f:
            f.write(response.text)
