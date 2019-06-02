# -*- coding: utf-8 -*-
import scrapy


class AutoSpider(scrapy.Spider):
    name = 'auto'
    allowed_domains = ['autocartruck.com']
    start_urls = ['https://www.autocartruck.com/umbraco/api/ServiceCenter/GetServiceCenters/?']

    def parse(self, response):
        pass

