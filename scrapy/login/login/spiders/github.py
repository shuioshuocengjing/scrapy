# -*- coding: utf-8 -*-
import scrapy
import re

class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        authenticity_token=response.xpath("//input[@name='authenticity_token']/@value").extract_first()
        utf8=response.xpath("//input[@name='utf8']/@value").extract_first()
        commit=response.xpath("//input[@name='commit']/@value").extract_first()
        post_data=dict(login='18701806870@163.com',
                       password='z0483451398',
                       authenticity_token=authenticity_token,
                       utf8=utf8,
                       commit=commit

                       )
        yield scrapy.FormRequest(
            "https://github/session",
            formdata=post_data,
            callback=self.after_login
        )
    def after_login(self,response):

        re.findall("noobpythoner|NooPythoner",response.body.decode())
    def parse1(self,response):
        yield scrapy.FormRequest.from_response(response,
                                               formdata={"login":"noobpythoner","password":"zhoudawe1123"},
                                               callback=self.after_login
                                               )
