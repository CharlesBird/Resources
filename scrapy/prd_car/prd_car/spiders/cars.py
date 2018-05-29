# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['prd.jlr-ecat.clifford-thames.com']
    start_urls = ['https://prd.jlr-ecat.clifford-thames.com/']

    def start_requests(self):
        return [Request('https://prd.jlr-ecat.clifford-thames.com/auth/realms/jlr/protocol/openid-connect/auth?client_id=gui&redirect_uri=https%3A%2F%2Fprd.jlr-ecat.clifford-thames.com%2F&state=73b3aa80-4a13-4eff-82da-a95cb80ae0b8&nonce=5e208b47-a257-4d1b-b842-28859f309ea8&response_mode=fragment&response_type=code&scope=openid',
                       headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'zh-CN,zh;q=0.9',
                                'referer': 'https://prd.jlr-ecat.clifford-thames.com/',
                                'upgrade-insecure-requests': 1,
                                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'},
                       callback=self.before_login)]

    def before_login(self, response):
        origin_url = response.url
        login_selec = response.xpath('//a[@class="zocial saml full-width"]')
        login_code = login_selec[1].xpath('@href').extract_first()
        # headers = {
        #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        #     'accept-encoding': 'gzip, deflate, br',
        #     'accept-language': 'zh-CN,zh;q=0.9',
        #     'referer': origin_url,
        #     'upgrade-insecure-requests': 1,
        #     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        headers = response.headers
        headers['referer'] = origin_url
        login_url = 'https://prd.jlr-ecat.clifford-thames.com' + login_code
        return [Request(login_url, headers=headers, callback=self.post_login)]

    def post_login(self, response):
        print(response)
        print(response.text)
        yield [Request()]
