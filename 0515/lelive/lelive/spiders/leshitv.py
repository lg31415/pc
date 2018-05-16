# -*- coding: utf-8 -*-
import scrapy
import json
from lelive.items import LeliveItem


class LeshitvSpider(scrapy.Spider):
    name = 'leshitv'
    allowed_domains = ['letv.com']
    page = 1
    url = 'http://dynamic.live.app.m.letv.com/android/dynamic.php?luamod=main&mod=live&ctl=liveHuya&act=channelList&pcode=010210000&version=7.13&channelId=2168&pages=' + str(
        page) + '&country=CN&provinceid=1&districtid=9&citylevel=1&location=%E5%8C%97%E4%BA%AC%E5%B8%82%7C%E6%9C%9D%E9%98%B3%E5%8C%BA&lang=chs&region=CN'
    start_urls = [url]

    def parse(self, response):
        item = LeliveItem()
        text = response.text
        dict_text = json.loads(text,encoding='utf-8')
        content = dict_text['body']['result']
        for every in content:
            # 主播名字
            item['nick_name'] = every.get('nick')
            # 主播的照片链接
            item['image_link'] = every.get('screenshot')
            # 主播的链接
            item['data_link'] = every.get('liveUrl')
            yield item

        # 请求下一页
        if self.page < 6:
            self.page += 1
        self.url = 'http://dynamic.live.app.m.letv.com/android/dynamic.php?luamod=main&mod=live&ctl=liveHuya&act=channelList&pcode=010210000&version=7.13&channelId=2168&pages=' + str(
        self.page) + '&country=CN&provinceid=1&districtid=9&citylevel=1&location=%E5%8C%97%E4%BA%AC%E5%B8%82%7C%E6%9C%9D%E9%98%B3%E5%8C%BA&lang=chs&region=CN'
        yield scrapy.Request(self.url,callback=self.parse)