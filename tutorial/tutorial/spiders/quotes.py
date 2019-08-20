# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrapy.com']
    start_urls = ['http://quotes.toscrapy.com/']

    def parse(self, response):
        qutoes = response.css('.quote')
        for qutoe in quotes:
            item = QuoteItem()
            item['text'] = qutoe.css('.text::text').extract_first()
            item['author'] = quote.css(' .author::text').extract_first() 
            item['tags'] = quote.css('.tags .tag::text').extract()
            yield item
        
        next = response.css('.pager .next a::attr("href")').extract_first()
        url =response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse)
