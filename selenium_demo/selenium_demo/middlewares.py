# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
from scrapy.http import HtmlResponse


class SeleniumMiddleware(object):

    def process_request(self, request, spider):
        url = request.url
        # chrome = webdriver.Chrome()
        spider.chrome.get(url)
        html = spider.chrome.page_source

        return HtmlResponse(url=url, body=html, request=request, encoding='utf-8')


