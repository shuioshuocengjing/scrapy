# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class TtSpider(CrawlSpider):
    # name = 'tt'
    # allowed_domains = ['tencent.com']
    # start_urls = ['http://hr.tencent.com/position.php']
    #
    # rules = (
    #     Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+&keywords=&tid=0&lid=0'), callback='parse_item'),
    #     Rule(LinkExtractor(allow=r'position_detail\.php\?&start=\d+#a'),follow=True)
    # )
    # def parse_item(self, response):
    #     item = {}
    #     item['title']=response.xpath("//td[@id='sharetitle']/text()").extract_first()
    #     item['aquire']=response.xpath("//div[text()='工作要求：']/../ul/li/text()").extract()
    #     return item
    ##第二种写法
    name = 'tt'
    allowed_domains = ['tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']

    rules = (
        #Rule(LinkExtractor(allow=r'position_detail\.php\?id=\d+&keywords=&tid=0&lid=0'), callback='parse_item'),
        Rule(LinkExtractor(allow=r'position_detail\.php\?&start=\d+#a'), callback='parse_item',follow=True)
    )

    def parse_item(self, response):
        tr_list=response.xpath("//table[@class='tablelist']/tr")[1:-1]
        for tr in tr_list:
            item={}
            item["title"]=tr.xpath("./td[1]/a/text()").extract_first()
            item["href"]='https://hr.tencent.com/'+tr.xpath("./td[1]/a/@href").extract_first()
            yield scrapy.Request(
                item['href'],
                callback=self.parse_detail,
                meta={"item":item}
            )
    def parse_detail(self,response):
        item=response.meta["item"]
        item['aquire']=response.xpath("//div[text()='工作要求：']/../ul/li/text()").extract()
        print(item)
