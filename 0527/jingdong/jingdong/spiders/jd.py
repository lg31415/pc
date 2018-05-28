# -*- coding: utf-8 -*-
import scrapy


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['sclub.jd.com']
    start_urls = ["https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv234&productId=3785639&score=0&sortType=5&page=1&pageSize=10&isShadowSku=0&rid=0&fold=1"
]

    def parse(self, response):
        print(response.text)
