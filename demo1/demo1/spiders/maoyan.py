# -*- coding: utf-8 -*-
import scrapy
from demo1.items import Demo1Item


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?offset=30']

    def parse(self, response):
        names = response.xpath('//div[@class="channel-detail movie-item-title"]/@title').extract()
        scores_div = response.xpath('//div[@class="channel-detail channel-detail-orange"]')

        scores = []
        for score in scores_div:
            scores.append(score.xpath('string(.)').extract()[0])

        for name, score in zip(names, scores):
            #print(name + ':' + score)
            # 推送字典
            yield {'name': name, 'score': score}

        item = Demo1Item()
        # for name, score in zip(names, scores_div):
        #     #print(name + ':' + score)
        #     # 推送Item对象
        #     item['name'] = name
        #     item['score'] = score
        #     yield item
