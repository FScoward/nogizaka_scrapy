# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NogizakaScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    entry_title = scrapy.Field()
    entry_body = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
