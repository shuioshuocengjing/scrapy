# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinaItem(scrapy.Item):
    # define the fields for your item here like:
    brand = scrapy.Field()
    dealer=scrapy.Field()
    address=scrapy.Field()
    phone=scrapy.Field()
    province=scrapy.Field()
    city=scrapy.Field()
    lat=scrapy.Field()
    lng=scrapy.Field()
    tel=scrapy.Field()



