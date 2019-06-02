# -*- coding: utf-8 -*-
import scrapy
from China.items import ChinaItem
import json

class VicoSpider(scrapy.Spider):
    name = 'Vico'
    allowed_domains = ['openapi.dlp.vwimport.cn']
    start_urls = ['https://openapi.dlp.vwimport.cn/openapi/dealer/dealerlist?callback=jQuery32105432680472146674_1558421995637&_=1558421995638']

    def parse(self, response):
        html=response.body.decode()[45:-2]
        print(html)
        html=json.loads(html)
        html=html['data']
        for ht in html:
            item = ChinaItem()
            item['brand'] = 'vico'
            item['address']=ht['address']
            item['city']=ht['cityName']
            item['phone']=ht['customerServiceTel']
            item['dealer']=ht['dealerName']
            item['lat']=ht['lat']
            item['lng']=ht['lng']
            item['province']=ht['provinceName']
            item['tel']=ht['tel']
            yield item



