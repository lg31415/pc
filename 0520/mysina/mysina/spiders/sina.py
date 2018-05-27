# -*- coding: utf-8 -*-
import os

import scrapy
from mysina.items import MysinaItem
from scrapy_redis.spiders import RedisSpider


class SinaSpider(RedisSpider):
    # 爬虫名字
    name = 'sinaspider_redis'
    # redis_key = 'sinaspider:start_urls'

    allowed_domains = ['sina.com.cn']
    #运行的时候使用redis_key。唯一
    redis_key = 'sinaspider:start_urls'
    # allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']


    # def __init__(self, *args, **kwargs):
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(SinaSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # 大标题与连接列表
        big_ac_title = response.xpath('//div[@id="tab01"]/div/h3/a/text()').extract()
        big_ac_url = response.xpath('//div[@id="tab01"]/div/h3/a/@href').extract()

        # 小标题与连接列表
        small_ac_title = response.xpath('//div[@id="tab01"]/div/ul/li/a/text()').extract()
        small_ac_url = response.xpath('//div[@id="tab01"]/div/ul/li/a/@href').extract()

        items = []

        for s in range(len(big_ac_url)):
            # 大目录
            big_path = './Data/' + big_ac_title[s]

            # 大连接
            big_ac_urls = big_ac_url[s]
            for j in range(len(small_ac_url)):
                item = MysinaItem()
                small_ac_urls = small_ac_url[j]
                # 判断是否属于大标题
                is_clcone = small_ac_urls.startswith(big_ac_urls)
                if is_clcone:
                    small_path = big_path + '/' + small_ac_title[j]

                    if not os.path.exists(small_path):
                        os.makedirs(small_path)
                    item['big_title'] = big_path
                    item['big_link'] = big_ac_urls

                    # 小
                    item['small_title'] = small_ac_title[j]
                    item['small_link'] = small_ac_urls
                    # 存储路径
                    item['small_path'] = small_path

                    items.append(item)

        for item in items:
            small_link = item['small_link']

            yield scrapy.Request(small_link, meta={'meta_item': item}, callback=self.seconde_parse, dont_filter=True)

    def seconde_parse(self, response):

        meta_item = response.meta['meta_item']

        links = response.xpath('//a/@href').extract()

        items = []
        for link in links:
            big_ac_link = meta_item['big_link']
            is_l = link.startswith(big_ac_link) and link.endswith('.shtml')
            if is_l:
                item = MysinaItem()
                # 存储大类
                item['big_title'] = meta_item['big_title']
                item['big_link'] = meta_item['big_link']
                # 存储小类
                item['small_title'] = meta_item['small_link']
                item['small_link'] = meta_item['small_link']
                item['small_path'] = meta_item['small_path']

                # 新加
                item['small_son_link'] = link
                # print(link)
                items.append(item)
        for item1 in items:
            small_son_links = item1['small_son_link']

            yield scrapy.Request(small_son_links, meta={'meta_item1': item1}, callback=self.three_parse, dont_filter=True)

    def three_parse(self, response):
        item = response.meta['meta_item1']
        ac_titles = response.xpath('//h1[@class="main-title"]/text()|//h1[@id="artibodyTitle"]/text()').extract()
        ac_contents = response.xpath('//div[@class="article"]//p/text()|//div[@id="artibody"]//p/text()').extract()
        ac_contents = ''.join(ac_contents)
        item['ac_title'] = ac_titles
        item['ac_content'] = ac_contents
        yield item
