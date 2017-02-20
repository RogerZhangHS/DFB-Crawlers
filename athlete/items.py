# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AthleteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    name = scrapy.Field()

class AthletePersonalInfo(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    age = scrapy.Field()
    sport = scrapy.Field()
    event = scrapy.Field()
    medal = scrapy.Field()
    country = scrapy.Field()
    result = scrapy.Field()
    