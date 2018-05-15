# -*- coding: utf-8 -*-
import scrapy
from two.items import AtguiguItem

class AtguiguSpider(scrapy.Spider):
    # 爬虫名字
    name = 'Atguigu'
    # 允许在哪个网站上爬取数据，可以去掉，可以在多个网站
    allowed_domains = ['www.atguigu.com']
    start_urls = ['http://www.atguigu.com/teacher.shtml']

    def parse(self, response):
    # //div[@class="teacher_content"]所有老师信息
    # 所有老师//div[@class="teacher_content"]/div/div/text()|//div[@class="teacher_content"]/p/text()
    # 老师简介//div[@class="teacher_content"]/text()
    # 老师图片//div[@class="teacher_content"]/img/@src
        # 所有老师信息
        item = AtguiguItem()
        # thachers = []
        teacher_list = response.xpath('//div[@class="teacher_content"]')
        for teacher in teacher_list:
            # 得到老师的照片
            teacher_img = teacher.xpath('./img/@src').get()  # 或者extract()转换成utf-8编码返回的还是列表
            # 得到老师的姓名
            teacher_name = teacher.xpath('./div/div/text()|./p/text()').extract()[0]
            # 得到老师的简介
            teacher_info = teacher.xpath('./text()').extract()
            # 拼接列表吧列表转换为字符串
            # 注意事项，key的名字是使用,items.py里面类的字段，
            teacher_info = "".join(teacher_info)
            item['name'] = teacher_name
            item['info'] = teacher_info
            item['image'] = teacher_img
            yield item
            # thachers.append(item)
            