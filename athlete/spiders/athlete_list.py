# -*- coding: utf-8 -*-
import scrapy
from athlete.items import AthleteItem


class AthleteListSpider(scrapy.Spider):
    name = "athlete_list"
    allowed_domains = ["www.databaseolympics.com"]
    start_urls = ['http://www.databaseolympics.com/players/playerlist.htm?lt=a',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=b',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=c',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=d',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=e',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=f',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=g',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=h',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=i',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=j',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=k',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=l',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=m',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=n',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=o',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=p',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=q',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=r',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=s',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=t',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=u',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=v',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=w',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=x',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=y',
                  'http://www.databaseolympics.com/players/playerlist.htm?lt=z']

    def parse(self, response):
        player_href = response.xpath('//a[contains(@href, "playerpage")]')
        items = []

        for site in player_href:
            item = AthleteItem()
            item['url'] = site.xpath('@href').extract()
            item['name'] = site.xpath('text()').extract()
            items.append(item)
        return items
