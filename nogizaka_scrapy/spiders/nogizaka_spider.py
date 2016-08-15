# -*- coding: utf-8 -*-

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from nogizaka_scrapy.items import NogizakaScrapyItem

class NogizakaSpider(CrawlSpider):
    name = "nogizaka_spider"
    allowed_domains = ['blog.nogizaka46.com']
    start_urls = ['http://blog.nogizaka46.com/']
    rules = (
        Rule(LinkExtractor(allow=r'/.*/\d{4}/\d{2}/.*\.php'), callback='parse_item', follow=True),
    )

    # parseだと何故か再帰的に探索しない
    def parse_item(self, response):
        # self.logger.info('================= url: %s', response.url)
        # self.logger.info('================= xpath: %s', response.xpath('//span[@class="entrytitle"]/text()').extract())
        item = NogizakaScrapyItem()
        item['entry_title'] = response.xpath('//span[@class="entrytitle"]/text()').extract()
        entry_body = response.xpath('//div[@class="entrybody"]/div/text()')
        # self.logger.info('================= body: %s', entry_body.extract())
        entry_body_array = []
        for body in entry_body:
            entry_body_array.append(body.extract())
        item['entry_body'] = ''.join(entry_body_array)
        self.logger.info('========================= %s', item['entry_body'])

        # filename = response.url.replace(":", "_").replace("/", "_").replace("?", "_") + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        return item
