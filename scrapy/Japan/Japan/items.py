# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JapanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    brand=scrapy.Field()
    dealer=scrapy.Field()
    address=scrapy.Field()
    tel=scrapy.Field()
    fax=scrapy.Field()
    lat=scrapy.Field()
    lng=scrapy.Field()
    province=scrapy.Field()
    city=scrapy.Field()


