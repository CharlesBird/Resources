# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request


class TopChinazPipeline(object):
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline(object):

    def open_spider(self, spider):
        self.file = open('items.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line)
        return item


class MyImagesPipeline(ImagesPipeline):
    """图片下载管道"""
    def get_media_requests(self, item, info):
        for image_url in item['image_url']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_result_url = [x['path'] for ok, x in results if ok]
        item['image_result_url'] = image_result_url
        return item
