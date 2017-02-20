# -*- coding: utf-8 -*-
import scrapy
from athlete.items import AthletePersonalInfo
import csv

class AthleteRecordsSpider(scrapy.Spider):
    name = "athlete_records"
    allowed_domains = ["http://www.databaseolympics.com"]
    url_csv = csv.reader(open("athlete_list.csv"))
    start_urls = []
    for row in url_csv:
        athlete_urls = "http://www.databaseolympics.com/players"+row[0]
        start_urls.append(athlete_urls)

    def parse(self, response):
        items = []
        resulttable = response.xpath('//table[@cellpadding=2]/tr[position()>1]')
        
        for trs in resulttable:
            item = AthletePersonalInfo()
            item['name'] = response.xpath('//h1/text()').extract()
            item['year'] = trs.xpath('td')[0].xpath('a/text()').extract()
            item['age'] = trs.xpath('td')[1].xpath('text()').extract()
            item['sport'] = trs.xpath('td')[2].xpath('a/text()').extract()
            item['event'] = trs.xpath('td')[3].xpath('a/text()').extract()
            item['medal'] = trs.xpath('td')[4].xpath('text()').extract()
            item['country'] = trs.xpath('td')[5].xpath('a/text()').extract()
            item['result'] = trs.xpath('td')[6].extract()[16:-5]
            items.append(item)
        
        return items
        
        
        
