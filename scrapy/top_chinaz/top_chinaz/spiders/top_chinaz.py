import scrapy
from scrapy import Request
import json
from ..items import TopChinazItem


class TopChinazSpider(scrapy.Spider):
    name = 'topchinaz'
    allowed_domains = ['top.chinaz.com']
    start_urls = ['http://top.chinaz.com/all/']

    def parse(self, response):
        """
        分页和详情页地址获取
        详情页地址：response.xpath('//div[@class="leftImg"]/a/@href').extract()
        下一页地址：response.xpath('//div[@class="ListPageWrap"]/a/@href').extract()[-1]
        """
        for href in response.xpath('//div[@class="leftImg"]/a/@href').extract():
            yield response.follow(href, callback=self.parse_detail)
        next_page = response.xpath('//div[@class="ListPageWrap"]/a/@href').extract()[-1]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_detail(self, response):
        """
        解析排名详情页
        获取跟节点赋值为：sel = response.xpath('//div[@class="TopPageCent clearfix"]')[0]"""
        item = TopChinazItem()
        sel = response.xpath('//div[@class="TopPageCent clearfix"]')[0]

