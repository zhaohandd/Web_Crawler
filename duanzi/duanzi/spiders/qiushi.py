# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider


class QiushiSpider(RedisCrawlSpider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    # start_urls = ['https://www.qiushibaike.com/text/']
    redis_key = 'qiushi:start_urls'
    rules = (
        Rule(LinkExtractor(allow=r'/article/\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/text/page/\d+/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
       content = response.xpath('//div[@class="content"]/text()').extract_first().strip()
       name = response.xpath('//h2/text()').extract_first().strip()

       yield {
           'name': name,
           'content': content
       }
