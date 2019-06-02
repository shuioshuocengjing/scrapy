# -*- coding: utf-8 -*-

import scrapy
import re
class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/327550029/profile']

    def start_requests(self):
        cookies=""
        cookies={i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
        yield scrapy.Request(self.start_urls[0],
                             callback=self.parse,
                             cookies=cookies
                             )

    def parse(self, response):
        print(re.findall("毛兆军",response.body.decode()))
        yield scrapy.Request(
            "",
            callback=self.parse_detail
        )
    def parse_detail(self,response):
        print(re.findall("毛兆军",response.body.decode()))

