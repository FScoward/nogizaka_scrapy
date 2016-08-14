# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NogizakaBlogSpider(CrawlSpider):
    name = 'nogizaka_blog'
    allowed_domains = ['blog.nogizaka46.com']
    start_urls = ['http://blog.nogizaka46.com/']

    rules = (
        # Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow='/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        self.logger.info('============================= url: %s', response.url)
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i
