# -*- coding: utf-8 -*-
import scrapy

from xiaoshuo.items import XiaoshuoItem


class ZwwSpider(scrapy.Spider):
    name = 'zww'
    allowed_domains = ['81zw.us']
    start_urls = ['https://www.81zw.us/book/606/424359.html']

    def parse(self, response):
        title = response.xpath('//h1/text()').extract_first()
        content = ''.join(response.xpath('//div[@id="content"]/text()').extract()).replace('\xa0\xa0\xa0\xa0', '\n')

        yield {
            'title': title,
            'content': content
        }


        next_url = response.xpath('//div[@class="bottem1"]/a[3]/@href').extract_first()
        # base_url = 'https://www.81zw.us/book/606/{}'.format(new_url)
        # yield scrapy.Request(base_url, callback=self.parse)
        # yield scrapy.Request(response.urljoin(next_url), callback=self.parse)

        if next_url.find('.html') != -1:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)

        item = XiaoshuoItem()

