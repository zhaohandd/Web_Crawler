# -*- coding: utf-8 -*-
import scrapy


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://hz.lianjia.com/ershoufang/pg{}/'.format(num) for num in range(1, 101)]

    def parse(self, response):
        urls = response.xpath('//div[@class="info clear"]/div[@class="title"]/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_info)

    def parse_info(self, response):
        # price = response.xpath('//span[@class="total"]')
        # unit = response.xpath('//span[@class="unit"]/span/text()')
        # 总价
        money = response.xpath('concat(//span[@class="total"],//span[@class="unit"]/span/text())').extract_first()
        # 单价
        unitPriceValue = response.xpath('string(//span[@class="unitPriceValue"])').extract_first()
        # 小区名称
        communityName = response.xpath('//div[@class="communityName"]/a[1]/text()').extract_first()
        # 所在区域
        areaName = response.xpath('string(//div[@class="areaName"]/span[@class="info"])').extract_first()
        # 可以看到有很多共同的标签，可以抽取出共同的标签，简化代码,如下表示
        # base = response.xpath('//div[@class="base"]//ul')
        # roomType = base.xpath('./li[1]/text()')
        # 户型
        roomType = response.xpath('//div[@class="base"]//ul/li[1]/text()').extract_first()
        # 所在楼层
        roomHeight = response.xpath('//div[@class="base"]//ul/li[2]/text()').extract_first()
        # 房屋面积
        roomArea = response.xpath('//div[@class="base"]//ul/li[3]/text()').extract_first()
        # 房屋装修
        roomChange = response.xpath('//div[@class="base"]//ul/li[9]/text()').extract_first()
        # 是否供暖
        roomHeat = response.xpath('//div[@class="base"]//ul/li[last()-2]/text()').extract_first()
        # 产权
        roomHost = response.xpath('//div[@class="base"]//ul/li[last()]/text()').extract_first()
        # 交易
        roomTransaction = response.xpath('//div[@class="transaction"]//ul')
        # 用途
        roomUse = response.xpath('//div[@class="base"]//ul/li[4]/span[2]/text()').extract_first()
        # 房屋年限
        roomAge = response.xpath('//div[@class="base"]//ul/li[last()-3]/span[2]/text()').extract_first()
        # 房屋抵押
        roomGive = response.xpath('//div[@class="base"]//ul/li[last()-1]/span[2]/text()').extract_first()

        yield {
            'money': money,
            'unitPriceValue': unitPriceValue,
            'communityName': communityName,
            'areaName': areaName,
            'roomType': roomType,
            'roomHeight': roomHeight,
            'roomArea': roomArea,
            'roomChange': roomChange,
            'roomHeat': roomHeat,
            'roomHost': roomHost,
            'roomUse': roomUse,
            'roomAge': roomAge,
            'roomGive': roomGive
        }








