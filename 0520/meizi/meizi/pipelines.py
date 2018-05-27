# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

import requests

from meizi.settings import IMAGES_STOER

class MeiziPipeline(object):
    def process_item(self, item, spider):
        if 'image' in item:
            images=[]

            image_path = '%s%s' % (IMAGES_STOER, spider.name )

            if not os.path.exists(image_path):
                os.makedirs(image_path)
            for image in item['image']:
                a = image.split('/')[3:]
                image_f_name = '_'.join(a)
                file_path = '%s%s' % (image_path, image_f_name)
                images.append(file_path)

                if os.path.exists(file_path):
                    continue

                response = requests.get(image)

                if response.status_code == 200:
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                else:
                    print('lose')
                item['image'] = image
        return item
