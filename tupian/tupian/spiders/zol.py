# -*- coding: utf-8 -*-
import scrapy


class ZolSpider(scrapy.Spider):
    name = 'zol'
    allowed_domains = ['zol.com.cn']
    start_urls = ['http://desk.zol.com.cn/bizhi/1974_25075_2.html']

    def parse(self, response):
        # 返回的是一个列表
        img_url = response.xpath('//img[@id="bigImg"]/@src').extract()
        img_name = response.xpath('string(//h3)').extract_first()
        yield {
            # 注意：一定要推送image_urls的字段
            "image_urls": img_url,
            "image_name": img_name
        }
        # url不完整，Request里的urljoin方法补全
        next_url = response.xpath('//a[@id="pageNext"]/@href').extract_first()
        # 找到最后一张图片
        if next_url.find('.html') != -1:
            yield scrapy.Request(response.urljoin(next_url), callback=self.parse)
