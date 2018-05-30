# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import random


class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['prd.jlr-ecat.clifford-thames.com']
    start_urls = ['https://prd.jlr-ecat.clifford-thames.com/']

    def start_requests(self):
        def get_size_chars(size):
            chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
            return ''.join(random.SystemRandom().choice(chars) for _ in range(size))
        state = '-'.join([get_size_chars(8), get_size_chars(4), get_size_chars(4), get_size_chars(4), get_size_chars(12)])
        nonce = '-'.join([get_size_chars(8), get_size_chars(4), get_size_chars(4), get_size_chars(4), get_size_chars(12)])

        url = 'https://prd.jlr-ecat.clifford-thames.com/auth/realms/jlr/protocol/openid-connect/auth?client_id=gui&redirect_uri=https%3A%2F%2Fprd.jlr-ecat.clifford-thames.com%2F&state={state}&nonce={nonce}&response_mode=fragment&response_type=code&scope=openid'
        yield Request(url=url.format(state=state, nonce=nonce),
                       headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                'accept-encoding': 'gzip, deflate, br',
                                'accept-language': 'zh-CN,zh;q=0.9',
                                'cookie': 'KC_RESTART=eyJhbGciOiJIUzI1NiIsImtpZCIgOiAiYWY3ODA5ZmQtYWY2Ni00OGM1LTgyMmMtNTFlZGIxM2NiNTgwIn0.eyJjcyI6Ijc3ZTI3MDNhLTg5ZDctNDZjNy1iMjgxLWYxODgyNWRjYTBmMCIsImNpZCI6Imd1aSIsInB0eSI6Im9wZW5pZC1jb25uZWN0IiwicnVyaSI6Imh0dHBzOi8vcHJkLmpsci1lY2F0LmNsaWZmb3JkLXRoYW1lcy5jb20vIiwiYWN0IjoiQVVUSEVOVElDQVRFIiwibm90ZXMiOnsiYXV0aF90eXBlIjoiY29kZSIsInNjb3BlIjoib3BlbmlkIiwiaXNzIjoiaHR0cHM6Ly9wcmQuamxyLWVjYXQuY2xpZmZvcmQtdGhhbWVzLmNvbS9hdXRoL3JlYWxtcy9qbHIiLCJyZXNwb25zZV90eXBlIjoiY29kZSIsInJlZGlyZWN0X3VyaSI6Imh0dHBzOi8vcHJkLmpsci1lY2F0LmNsaWZmb3JkLXRoYW1lcy5jb20vIiwic3RhdGUiOiIzM2E1ZjVlYS0yN2U5LTQ2MDUtODdlNS03Zjc4MzBkNGE5NDYiLCJub25jZSI6IjdkMmRkYzdkLThlODUtNGZmNC04OGZjLTUwMjkwODkxNzU1ZCIsInJlc3BvbnNlX21vZGUiOiJmcmFnbWVudCJ9fQ.K2YghXpn__D8NDjzUuPvQQtHPeMR0pvTqDzZl0uDAD4',
                                'referer': 'https://prd.jlr-ecat.clifford-thames.com/',
                                'upgrade-insecure-requests': 1,
                                'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'},
                       callback=self.before_login)

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
        yield Request(login_url, headers=headers, callback=self.post_login)

    def post_login(self, response):
        print(response)
        print(response.text)
        yield Request()
