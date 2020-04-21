# -*- coding: utf-8 -*-
import scrapy
# 文件目录下执行 scrapy crawl test（项目名称）

class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']

    def parse(self, response):
        print('=====\n')
        print(type(response))
        print('=====\n')
