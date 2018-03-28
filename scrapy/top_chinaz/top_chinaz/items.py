# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class TopChinazItem(Item):
    # define the fields for your item here like:
    name = Field()
    link = Field()
    pstar = Field()
    dateup = Field()
    total_ranking = Field()
    region = Field()
    region_ranking = Field()
    hangye = Field()
    hangye_ranking = Field()
    image_url= Field()
    webIntro = Field()
    image_result_url = Field()
