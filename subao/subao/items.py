# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SubaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class PersonInfoItem(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()
    salary = scrapy.Field()
    phone = scrapy.Field()
