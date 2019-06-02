# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
import re

class CtripSpider(scrapy.Spider):
    name = 'ctrip'
    allowed_domains = ['ctrip.com']
    start_urls = ['https://hotels.ctrip.com/hotel/baotou141/p1']

    def parse(self, response):
        item={}
        hotel_urls=response.xpath("//div[@id='hotel_list']/div")[0]
        #for hotel_url in hotel_urls:
        item['name']=hotel_urls.xpath(".//h2[@class='hotel_name']/a/@title").extract_first()
        item['href']=urllib.parse.urljoin('https://hotel.ctrip.com',hotel_urls.xpath(".//h2[@class='hotel_name']/a/@href").extract_first())
        yield scrapy.Request(item['href'],
                       callback=self.parse_detail,
                       meta={'item':item})
        # html='https://hotel.ctrip.com/hotel/baotou141/p'
        # for i in range(2,26):
        #     scrapy.Request(html+str(i),
        #                    callback=self.parse,
        #                    meta={'item':item}
        #                    )
    def parse_detail(self,response):
        item = response.meta["item"]
        print(response.body.decode())
        name=re.findall('<a rel="nofollow".*?>.*?"(.*?)".*?<br>',response.body.decode(),re.S)
        # print(name)




