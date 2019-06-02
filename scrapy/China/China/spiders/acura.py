# -*- coding: utf-8 -*-
import scrapy
import json
from China.items import ChinaItem
import copy
#scrapy crawel Vico -o vico.csv
class AcuraSpider(scrapy.Spider):
    name = 'acura'
    allowed_domains = ['acura.ghac.cn']
    start_urls = ['http://www.acura.ghac.cn/api/sitecore/Common/GetProvinceFilterByDealer']

    def parse(self, response):
        html=response.body.decode()
        dicts=json.loads(html)['Data']
        formdata = {}
        for dt in dicts:
            item=ChinaItem()
            item['brand']='acura'
            item['province']=dt['Name']
            formdata['provinceId']=dt['Id']
            yield scrapy.FormRequest('http://www.acura.ghac.cn/api/sitecore/Common/GetCityFilterByDealer',
                                     formdata=formdata,
                                     callback=self.parse_city,
                                     meta={'item':item})
    def parse_city(self,response):
        item=response.meta['item']
        citys=response.body.decode()
        print(citys)
        citys=json.loads(citys)['Data']
        formdata={}
        for city in citys:
            item['city']=city['Name']
            formdata['cityId']=city['Id']
            print('----------------',city['Name'])
            yield scrapy.FormRequest('http://www.acura.ghac.cn/api/sitecore/Map/GetDealerList',
                                     formdata=formdata,
                                     callback=self.parse_detail,
                                     meta={'item':copy.deepcopy(item)})
    def parse_detail(self,response):
        item=response.meta['item']
        getlists=response.body.decode()
        getlists=json.loads(getlists)['Data']
        for getlist in getlists:
            item['address']=getlist['ADDRESS']
            item['dealer']=getlist['DEALER_NAME']
            item['lat']=getlist['Lat']
            item['lng']=getlist['Lng']
            item['phone']=getlist['SALES_PHONE']
            yield item







