# -*- coding: utf-8 -*-
import scrapy
from Japan.items import JapanItem
import copy
class CadillacSpider(scrapy.Spider):
    name = 'cadillac'
    allowed_domains = ['cadillacjapan.com','gmj-dealer.jp']
    start_urls = ['http://www.cadillacjapan.com/tools/locate_dealer.html']

    def parse(self, response):
        item=JapanItem()
        item['brand']='cadillac'
        japan_list=response.xpath("//div[@class='fck_authorsinput cta_txt tx']/p")
        for jap in japan_list:
            item['dealer']=jap.xpath(".//span/text()").extract_first()
            url=jap.xpath(".//a/@href").extract_first()
            yield scrapy.Request(url,callback=self.parse_detail,meta={'item':copy.deepcopy(item)})
    def parse_detail(self,response):
        item=response.meta['item']
        item['address']=response.xpath("//div[@class='dis_flex infoArea_section']/a/text()").extract_first()
        item['tel']=response.xpath("//div[@class='dis_flex infoArea_section']/div/a/text()").extract_first()
        yield item

