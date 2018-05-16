# -*- coding: utf-8 -*-
import scrapy
import json
from leshilive.items import LeshiliveItem


class LeshitvSpider(scrapy.Spider):
    name = 'leshitv'
    allowed_domains = ['letv.com']
    page = 1
    url = 'http://dynamic.live.app.m.letv.com/android/dynamic.php?luamod=main&mod=live&ctl=liveHuya&act=channelList&pcode=010210000&version=7.13&channelId=2168&pages=' + str(
        page) + '&country=CN&provinceid=1&districtid=9&citylevel=1&location=%E5%8C%97%E4%BA%AC%E5%B8%82%7C%E6%9C%9D%E9%98%B3%E5%8C%BA&lang=chs&region=CN'
    start_urls = [url]

    def parse(self, response):
        content = json.loads(response.text, encoding='utf-8')
        item = LeshiliveItem()
        content1 = content['body']['result']
        for ev in content1:
            item['nick_name'] = ev.get('nick')
            # 主播的照片链接
            item['image_link'] = ev.get('screenshot')
            # 房间
            item['data_link'] = ev.get('liveUrl')
            yield item
        if self.page < 10:
            self.page += 1
        self.url = 'http://dynamic.live.app.m.letv.com/android/dynamic.php?luamod=main&mod=live&ctl=liveHuya&act=channelList&pcode=010210000&version=7.13&channelId=2168&pages=' + str(
        self.page) + '&country=CN&provinceid=1&districtid=9&citylevel=1&location=%E5%8C%97%E4%BA%AC%E5%B8%82%7C%E6%9C%9D%E9%98%B3%E5%8C%BA&lang=chs&region=CN'
        yield scrapy.Request(self.url, callback=self.parse)