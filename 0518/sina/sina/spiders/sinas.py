# -*- coding: utf-8 -*-
import scrapy
import os
from sina.items import SinaItem


class SinasSpider(scrapy.Spider):
    name = 'sinas'
    allowed_domains = ['sina.com']
    start_urls = ['http://news.sina.com.cn/guide/']

    def parse(self, response):
        # 返回的是:新闻,体育,娱乐等等大标题列表 
        parent_titles = response.xpath('//div[@id="tab01"]/div/h3/a/text()').extract()
        # 返回的是:新闻,体育,娱乐等等大标题链接列表
        parent_urls = response.xpath('//div[@id="tab01"]/div/h3/a/@href').extract()

        sub_titles = response.xpath('//div[@id="tab01"]/div/ul/li/a/text()').extract()

        sub_urls = response.xpath('//div[@id="tab01"]/div/ul/li/a/@href').extract()

        son_urls = response.xpath('//div[@id="tab01"]/div/ul/li/a/@href').extract()

        items = []
        for i in range(len(parent_urls)):
            item = SinaItem()
            # 大类的目录 
            parent_file = "./Data/" + parent_titles[i]
            # 大类的url:http://news.sina.com.cn/ 
            parent_url = parent_urls[i]
            for j in range(len(sub_urls)):
                # 小类的url:http://news.sina.com.cn/china/ 
                # 大类和小类标题前缀相同都是:http://news.sina.com.cn/ 
                sub_url = sub_urls[j]
                # 判断小类的标题是否属于大类标题 
                is_belong = sub_url.startswith(parent_url)
                if is_belong:
                    # .Data/新闻/国内,.Data/新闻/国际
                    sub_file = parent_file + "/" + sub_titles[j]
                    # 创建目录,先判断目录是否存在,如果不存在再创建目录 
                    if not os.path.exists(sub_file):
                        os.makedirs(sub_file)

                    item["parent_title"] = parent_file
                    item["parent_urls"] = parent_url
                    item["sub_title"] = sub_titles[j]
                    item["sub_urls"] = sub_url
                    item["sub_file_name"] = sub_file
                    item['son_urls'] = son_urls
                    items.append(item)
                    for item in items:
                        sub_url = item['sub_urls']
                        sub_title = item['sub_title']
                        yield scrapy.Request(url=sub_url, meta={'meta_item':item}, callback=self.second_parse)
                    for s in items:
                        geandson_url = s["son_urls"]
                        yield scrapy.Request(url=geandson_url, meta={'meta_item2': s}, callback=self.deatil_parse)

    def second_parse(self,response):
            meta_item = response.meta['meta_item']
            urls = response.xpath('//a/@href').extract()
            items=[]
            for u in urls:
                parent_url = meta_item['parent_urls']

                is_belong = u.startswith(parent_url) and u.endswith('.shtml')

                if is_belong:
                    item = SinaItem()
                    item['parent_title'] = meta_item['parent_title']
                    item['parent_urls'] = meta_item['parent_urls']

                    item['sub_title'] = meta_item['sub_title']
                    item['sub_urls'] = meta_item['sub_urls']
                    item['sub_file_name'] = meta_item['sub_file_name']


                    item['son_urls'] = u
                    items.append(item)
                    yield items

    def deatil_parse(self,response):
        meta_item2 = response.meta['meta_item2']
        genderson_title = response.xpath('//h1[@class="artibodyTitle"]/text()|//h1[@class="main-title"]/text()').extract()
        genderson_title = ''.join(genderson_title)
        genderson_content = response.xpath('//div[@id="article"]/p[position()>1]/text()|//div[@id="artibody"]/p/text()').extract()
        genderson_content = ''.join(genderson_content)
        meta_item2['genderson_title'] = genderson_title
        meta_item2['genderson_content'] = genderson_content
        print( meta_item2)