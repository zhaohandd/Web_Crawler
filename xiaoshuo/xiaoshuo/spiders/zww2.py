# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Zww2Spider(CrawlSpider):
    name = 'zww2'
    allowed_domains = ['81zw.us']
    start_urls = ['https://www.81zw.us/book/1215/']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=r'//dl/dd[2]/a'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=r'//div[@class="bottem1"]/a[3]'), callback='parse_item', follow=True)
    )

    def parse_item(self, response):
        # i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i


        title = response.xpath('//h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract()).replace('\xa0\xa0\xa0\xa0', '\n')
        yield {
            'title': title,
            'content': content
        }