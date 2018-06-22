# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request
from scrapy.conf import settings
import pymongo


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


class MongoPipeline(object):

    def __init__(self):
        self.host = settings['MONGODB_HOST']
        self.port = settings['MONGODB_PORT']
        self.mongo_db = settings['MONGODB_DBNAME']
        self.coll = settings['MONGODB_DOCNAME']
        self.user = settings['MONGODB_USER']
        self.pwd = settings['MONGODB_PWD']

    def open_spider(self, spider):
        """
        添加用户验证
        :param spider:
        :return:
        """
        self.client = pymongo.MongoClient(host=self.host, port=self.port)
        self.db = self.client[self.mongo_db]
        self.db.authenticate(self.user, self.pwd)

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        postitem = dict(item)
        self.db[self.coll].update({'link': postitem["link"], 'dateup': postitem["dateup"]}, {'$set': postitem}, True)
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
