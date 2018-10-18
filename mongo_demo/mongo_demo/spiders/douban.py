# -*- coding: utf-8 -*-
import scrapy


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start={}&filter='.format(num) for num in range(0, 250, 25)]

    def parse(self, response):
        names = response.xpath('//div[@class="hd"]/a/span[1]/text()').extract()
        stars = response.xpath('//span[@class="rating_num"]/text()').extract()
        for name, star in zip(names, stars):
            yield {
                'name': name,
                'star': star,
            }
