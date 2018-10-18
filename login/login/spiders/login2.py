# -*- coding: utf-8 -*-
import scrapy


class Login2Spider(scrapy.Spider):
    name = 'login2'
    allowed_domains = ['sxt.cn']
    start_urls = ['https://www.sxt.cn/index/user.html']

    def start_requests(self):
        cookies_str = 'acw_tc=7b39758215363011943874835e1d3215bb94a146b06916441ade66e322bb46;' \
                      ' UM_distinctid=165b2b21496193-0101c13d25471b-323b5b03-1fa400-165b2b21498c8;' \
                      ' NTKF_T2D_CLIENTID=guest198E67AC-C852-3A32-8764-B2B2166CCDA7; ' \
                      '53gid2=10402417542006; 53revisit=1536301341404; PHPSESSID=hfre9ei0353c1f5np18go34m87; ' \
                      'G_WPT_TO=zh-CN; SL_GWPT_Show_Hide_tmp=1; ' \
                      'CNZZDATA1261969808=433646691-1536299364-%252F%252Fwww.sxt.cn%252F%7C1538878802;' \
                      ' nTalk_CACHE_DATA={uid:kf_10279_ISME9754_guest198E67AC-C852-3A,tid:1538882345224107};' \
                      ' visitor_type=old; 53gid0=10402417542006; 53gid1=10402417542006; ' \
                      '53kf_72085067_from_host=www.sxt.cn; 53kf_72085067_keyword=https%3A%2F%2Fwww.sxt.cn%2Findex%2Flogin%2Flogin.html; ' \
                      '53kf_72085067_land_page=https%253A%252F%252Fwww.sxt.cn%252Findex.html;' \
                      ' kf_72085067_land_page_ok=1; ' \
                      'nTalk_PAGE_MANAGE={|m|:[{|67037|:|827046|},{|90327|:|827042|}],|t|:|11:25:04|}'
        cookies = {}
        for cookie in cookies_str.split(';'):
            key ,value = cookie.split('=', 1)
            cookies[key.strip()] = value.strip()
        yield scrapy.Request(url='https://www.sxt.cn/index/user.html',cookies=cookies, callback=self.parse)

    def parse(self, response):
        print(response.text)
