import scrapy
from scrapy import Request
import json
from ..items import TopChinazItem


class TopChinazSpider(scrapy.Spider):
    name = 'topchinaz'
    allowed_domains = ['www.zhihu.com']
    start_urls = ['http://top.chinaz.com/']

    def parse(self, response):
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse)