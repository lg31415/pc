# -*- coding: utf-8 -*-
import scrapy


class AtguiguSpider(scrapy.Spider):
    name = 'Atguigu'
    allowed_domains = ['www.atguigu.com']
    start_urls = ['http://www.atguigu.com/teacher.shtml']

    def parse(self, response):
        content = response.body.decode('utf-8')
        filename = "teacher.html"
        print(content)
        open(filename, 'w', encoding='utf-8').write(content)
