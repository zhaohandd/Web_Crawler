import requests
from fake_useragent import UserAgent
from lxml import etree

#中国新闻网
url = 'http://www.chinanews.com/gn/2018/09-13/8625925.shtml'
headers = {
    'User-agent': UserAgent().random
}
response = requests.get(url, headers=headers)
response.encoding = 'gbk'
# print(response.text)

e = etree.HTML(response.text)
title = e.xpath('//h1/text()')
content = e.xpath('//div[@class="content"]//p/text()')
img_urls = e.xpath('//div[@class="content"]//img/@src')
img_contents = e.xpath('//div[@class="content"]//img/@title')

for img_content, img_url in zip(img_urls, img_contents):
    print(img_url + img_content)


