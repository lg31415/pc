# -*- coding: utf-8 -*-
import scrapy


class RrwSpider(scrapy.Spider):
    name = 'rrw'
    # allowed_domains = ['renren.com']
    # start_urls = ['http://renren.com/']
    # spider的post请求

    def start_requests(self):
        yield scrapy.FormRequest(
            url='http://www.renren.com/PLogin.do',
            formdata={'email': 'yangguangfu2017@163.com', 'password': 'afu123456'},
            callback=self.parse
        )

    def parse(self, response):
        print(response.text)
