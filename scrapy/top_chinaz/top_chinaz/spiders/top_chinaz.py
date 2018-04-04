import scrapy
from scrapy import Request
import json
import re
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

        header = response.xpath('//div[@class="TopPageCent clearfix"]/div[@class="TPageCent-header"]')
        if header:
            name = header[0].xpath('h2/text()').extract_first()
            link = header[0].xpath('p[1]/a/@href').extract_first()
            pstar_url = header[0].xpath('p[2]/img/@src').extract_first()
            dateup = header[0].xpath('span/text()').extract_first()
            item['name'] = name
            item['link'] = link
            item['pstar'] = pstar_url and re.search(r'\d{1}', pstar_url).group()
            item['dateup'] = dateup and dateup[5:]

        topmain = response.xpath('//div[@class="TopPageCent clearfix"]/div[@class="TPageCent-TopMain mt10 clearfix"]')
        if topmain:
            total_ranking = topmain[0].xpath('ul/li[1]/p[1]/a/text()').extract_first()
            region_ranking = topmain[0].xpath('ul/li[2]/p[1]/a/text()').extract_first()
            region = topmain[0].xpath('ul/li[2]/p[2]/a/text()').extract_first()
            hangye_ranking = topmain[0].xpath('ul/li[3]/p[1]/a/text()').extract_first()
            hangye = topmain[0].xpath('ul/li[3]/p[2]/a/text()').extract_first()
            item['total_ranking'] = total_ranking
            item['region_ranking'] = region_ranking
            item['region'] = region
            item['hangye_ranking'] = hangye_ranking
            item['hangye'] = hangye

        tmain01 = response.xpath('//div[@class="TopPageCent clearfix"]/div[@class="TPageCent-TMain01 mb40"]')
        if tmain01:
            image_url = tmain01[0].xpath('div[1]/div[@class="Centleft fl mt5"]/img/@src').extract_first()
            webIntro = tmain01[0].xpath('div[1]/div[@class="Centright fr SimSun"]/p/text()').extract_first()
            item['image_url'] = image_url and ['http:' + image_url] or []
            item['webIntro'] = webIntro

        mb30 = response.xpath('//div[@class="CobaseCon mb30"]')
        if mb30:
            spans = mb30[0].xpath('ul/li[2]/span/text()').extract()
            try:
                company_name, legal_representative, registered_capital, registered_date = spans
                item['company_name'] = company_name
                item['legal_representative'] = legal_representative
                item['registered_capital'] = registered_capital
                item['registered_date'] = registered_date
            except ValueError as e:
                pass

        yield item


