# -*- coding: utf-8 -*-
import scrapy
import re


class Login3Spider(scrapy.Spider):
    name = 'login3'
    allowed_domains = ['ganji.com']
    start_urls = ['https://passport.ganji.com/login.php']

    def parse(self, response):
        hash_code = re.findall(r'"__hash__":"(.+)"', response.text)[0]
        img_url = response.xpath('//label[@class="label-imgcode"]/img[@class="login-img-checkcode"]/@src').extract_first()
        yield scrapy.Request(img_url, callback= self.parse_info, meta={'hash_code': hash_code})

    def parse_info(self, response):
        hash_code = response.request.meta['hash_code']
        with open('yzm.jpg', 'wb') as f:
            f.write(response.body)

        code = input('please input check-code : ')

        form_data = {
            'username': '17703181473',
            'password': '123456abcd',
            'setcookie': '0',
            'checkCode': code,
            'next': '/',
            'source': 'passport',
            '__hash__': hash_code
        }

        yield scrapy.FormRequest(url='https://passport.ganji.com/login.php', callback=self.after_login)

    def after_login(self, response):
        print(response.text)