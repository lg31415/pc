# -*- coding: utf-8 -*-
import json

import scrapy

from Acfun.items import AcfunItem


class Acfu2Spider(scrapy.Spider):
    name = 'acfu2'
    allowed_domains = ['acfun.cn']
    offset = 1
    url = 'http://www.acfun.cn/list/getlist?channelId=107&sort=0&pageSize=20&pageNo='
    start_urls = [url+str(offset)]

    def parse(self, response):
        json_text = response.text
        dict_python = json.loads(json_text, encoding='utf-8')
        content = dict_python['data']['data']

        for e in content:
            item = AcfunItem()
            # 获取连接
            urls = 'http://www.acfun.cn' + e.get('link')
            # 获取番剧主题
            ac_title = e.get('title')
            # 获取作者昵称
            ac_name = e.get('username')
            # 获取发布时间
            ac_time = e.get('contributeTimeFormat')
            # 获取作者的空间连接
            ac_home = e.get('userUrl')
            # 获取播放次数
            ac_nums = e.get('viewCountFormat')

            item['names'] = ac_name
            item['titles'] = ac_title
            item['times'] = ac_time
            item['video_link'] = urls
            item['homeb'] = ac_home
            item['numbers'] = ac_nums
            yield item
        if self.offset < 774:
            self.offset += 1
            url = self.url + str(self.offset)
            yield scrapy.Request(url,callback=self.parse)
