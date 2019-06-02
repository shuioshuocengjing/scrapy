# -*- coding: utf-8 -*-
import scrapy
import requests
import json
from China.items import ChinaItem
class MiniSpider(scrapy.Spider):
    name = 'mini'
    allowed_domains = ['minichina.com.cn']
    start_urls = ['https://www.minichina.com.cn/zh_CN/home/dlo.html']

    def parse(self, response):
        header={'Referer':'https://www.minichina.com.cn/zh_CN/home/dlo.html',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
        text=requests.get('https://cn-digital2-app.bmw.com.cn/dlo/init?',params={'callbackparam':'CALLBACK','brands':'2','_':'1558492401782'},headers=header)
        provinces={}
        text=json.loads(text.content.decode()[9:-1])
        text=text['responseBody']
        provs=text['provinces']
        cities=text['cities']
        item=ChinaItem()
        item['brand']='mini'
        param={'callbackparam':'CALLBACK','province':'ccccc750932','city':'sfs','serviceCodes':'','brands':'2','_':'1558492401783'}
        for pro in provs:
            provinces[pro['id']]=pro['nz']
        for city in cities:
            item['province']=provinces.get(city['pv'],'')
            item['city']=city['nz']
            param['province']=city['pv']
            param['city']=city['id']
            text=requests.get('https://cn-digital2-app.bmw.com.cn/dlo/outlet?',headers=header,params=param)
            text = json.loads(text.content.decode()[9:-1])
            text=text['responseBody']['outlets']
            for tx in text:
                item['address']=tx['az']
                item['phone']=tx['fax']
                item['dealer']=tx['nz']
                item['lat']=tx['ltb']
                item['lng']=tx['lnb']
                item['tel']=tx['tel']
                yield item
    #         yield scrapy.FormRequest('https://cn-digital2-app.bmw.com.cn/dlo/outlet?',headers=header,callback=self.parse_detail,meta={'item':copy.deepcopy(item)},method='GET',
    #                                  formdata=param)
    # def parse_detail(self,response):
    #     item=response.meta['item']
    #     text=json.loads(response.body.decode())[9:-1]
    #     text=text['responseBody']['outlets']
    #     print(text)
    #     if len(text)>1:
    #         for tx in text:
    #             item['address']=tx['az']
    #             item['phone']=tx['fax']
    #             item['dealer']=tx['nz']
    #             item['lat']=tx['ltb']
    #             item['lng']=tx['lng']
    #             item['tel']=tx['tel']
    #             yield item
    #     else:
    #         item['address'] = text['az']
    #         item['phone'] = text['fax']
    #         item['dealer'] = text['nz']
    #         item['lat'] = text['ltb']
    #         item['lng'] = text['lng']
    #         item['tel'] = text['tel']
    #         yield item

