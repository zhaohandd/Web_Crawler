# -*- coding: utf-8 -*-
import scrapy


class QidianSpider(scrapy.Spider):
    name = 'qidian'
    allowed_domains = ['qidian.com']
    start_urls = ['https://www.qidian.com/rank/yuepiao']

    def parse(self, response):
        # print(response.text)
        names = response.xpath('//h4/a/text()').extract()
        authors = response.xpath('//p[@class="author"]/a[1]/text()').extract()
        # print(names)
        # print(authors)
        book = []
        for name, author in zip(names, authors):
            book.append({'name': name, 'author': author})
        return book
