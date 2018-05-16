# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Dongguan.items import DongguanItem


class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    allowed_domains = ['wz.sun0769.com']

    offset = 0

    url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page=' + str(offset)

    start_urls = [url]

    rules = (
        Rule(LinkExtractor(allow=r'type=4')),
        Rule(LinkExtractor(allow=r'/question/\d+/\d+.shtml'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        print(self.offset)
        item = DongguanItem()
        # page = response.xpath('//div[@class="greyframe"]//div[@class="pagination"]//span[@class="cur"]/text()').get()
        # print('================', page)
        #帖子的链接
        urls = response.url
        # 帖子的标题
        titles = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        titless = titles.split("\xa0\xa0")[0].split("：")[1]
        # 编号
        nums = titles.split("\xa0\xa0")[1].split(":")[1]
        # 帖子的内容
        contents = response.xpath('//div[@class="content text14_2"]/div[@class="c1 text14_2"]/text()').extract()
        if contents == 0:
            contents = response.xpath('//div[@class="c1 text14_2"]/text()').extract()
            contents = ''.join(contents)
        else:
            contents = ''.join(contents)

        item['title'] = titless
        item['number'] = nums
        item['url'] = urls
        item['content'] = contents
        yield item

    def parse(self, response):
        # 所有帖子的链接
        text = response.url

        # 请求匹配的链接
        link = response.xpath('//a[contains(@href,"/html/question")]/@href').extract()
        print(link)
        for i in link:
            # 帖子标题
            yield scrapy.Request(i, callback=self.parse_item)

        if self.offset < 90750:
            self.offset += 30
            url = self.url + str(self.offset)
            yield scrapy.Request(url, callback=self.parse)