# -*- coding: utf-8 -*-
import scrapy
from three.items import ThreeItem


class AtguiguSpider(scrapy.Spider):
    name = 'Atguigu'
    allowed_domains = ['www.atguigu.com']
    start_urls = ['http://www.atguigu.com/teacher.shtml']

    def parse(self, response):
        item = ThreeItem()
        teacher_list = response.xpath('//div[@class="teacher_content"]')
        for teacher in teacher_list:
            # 得到老师的照片
            teacher_img = teacher.xpath('./img/@src').get()  # 或者extract()转换成utf-8编码返回的还是列表
            # 得到老师的姓名
            teacher_name = teacher.xpath('./div/div/text()|./p/text()').extract()[0]
            # 得到老师的简介
            teacher_info = teacher.xpath('./text()').extract()
            item['name'] = teacher_name
            item['image'] = teacher_img
            item['info'] = teacher_info
            yield item