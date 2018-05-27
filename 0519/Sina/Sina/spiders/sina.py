# -*- coding: utf-8 -*-
import scrapy
import os
from Sina.items import SinaItem


class SinaSpider(scrapy.Spider):
    name = 'sina'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        parent_title = response.xpath('//div[@id="tab01"]/div/h3/a/text()').extract()
        parent_url = response.xpath('//div[@id="tab01"]/div/h3/a/@href').extract()
        son_title = response.xpath('//div[@id="tab01"]/div/ul/li/a/text()').extract()
        son_url = response.xpath('//div[@id="tab01"]/div/ul/li/a/@href').extract()

        item = []

        for i in range(len(parent_url)):
            # 用自己的名字创建文件夹
            parent_titles = './Data/' + parent_title[i]
            parent_urls = parent_url[i]

            for j in range(len(son_url)):
                son_titles = son_title[j]
                son_urls = son_url[j]

                if son_urls.startswith(parent_urls):
                    items = SinaItem()
                    parent_path = parent_titles + "/" + son_titles

                    if not os.path.exists(parent_path):
                        os.makedirs(parent_path)

                    items["parent_title"] = parent_titles
                    items["parent_url"] = parent_urls
                    items["son_title"] = son_titles
                    items["son_url"] = son_urls
                    items["parent_path"] = parent_path
                    item.append(items)
                    # print(item)

            # 请求第二层循环
            for x in item:
                son_urls = x['son_url']

                yield scrapy.Request(son_urls, callback=self.second_parse, meta={"meta_item": x})

    def second_parse(self, response):
        meta_item = response.meta['meta_item']
        # print(type(meta_item))
        url_list = response.xpath('//a/@href').extract()
        items = []
        for i in url_list:
            parent_urls = meta_item['parent_url']
            # print('=' * 50, parent_urls)
            if i.startswith(parent_urls) and i.endswith('.shtml'):
                item = SinaItem()
                sun_url = i
                # print('=' * 50, sun_url)
                item['parent_title'] = meta_item['parent_title']
                item['parent_url'] = meta_item['parent_url']
                item['son_title'] = meta_item['son_title']
                item['son_url'] = meta_item['son_url']
                item["parent_path"] = meta_item['parent_path']
                item['grandson_url'] = sun_url
                items.append(item)
        # 第三层
        for a in items:
            sun_url = a['grandson_url']
            yield scrapy.Request(sun_url, callback=self.three_parse, meta={'meta_item1': a})

    def three_parse(self, response):
        meta_item = response.meta['meta_item1']

        sun_title = response.xpath('//h1[@id="artibodyTitle"]/text()|//h1[@class="main-title"]/text()').extract()
        sun_title = ''.join(sun_title)

        sun_content = response.xpath('//div[@id="article"]/p[position()>1]/text()|//div[@id="artibody"]/p/text()').extract()

        sun_content = ''.join(sun_content)

        meta_item['grandson_title'] = sun_title
        meta_item['grandson_content'] = sun_content
        # print('==============================', sun_content)
        yield meta_item
