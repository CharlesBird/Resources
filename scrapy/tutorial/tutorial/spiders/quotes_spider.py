# -*- coding: utf-8 -*-

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url += 'tag/' + tag
        yield scrapy.Request(url=url, callback=self.parse)

    # start_urls = [
    #     'http://quotes.toscrape.com/',
    #     # 'http://quotes.toscrape.com/page/2/',
    # ]

    # def parse(self, response):
    #     page = response.url.split('/')[-2]
    #     filename = 'quotes-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
        # self.log('Saved file %s' % filename)

    # def parse(self, response):
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'text': quote.css('span.text::text').extract_first(),
    #             'author': quote.css('small.author::text').extract_first(),
    #             'tags': quote.css('div.tags a.tag::text').extract()
    #         }
    #     next_page = response.css('li.next a::attr(href)').extract_first()
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         yield scrapy.Request(next_page, callback=self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('small.author::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract()
            }
        yield response.follow(response.css('li.next a')[0], callback=self.parse)
        # for a in response.css('li.next a'):
        #     yield response.follow(a, callback=self.parse)
        # for href in response.css('li.next a::attr(href)'):
        #     yield response.follow(href, callback=self.parse)
        # next_page = response.css('li.next a::attr(href)').extract_first()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)


class AuthorSpider(scrapy.Spider):
    name = "author"

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, callback=self.parse_author)

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, callback=self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).extract_first().strip()
        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text')
        }