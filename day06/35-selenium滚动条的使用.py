from selenium import webdriver
from lxml import etree
from time import sleep

chrome = webdriver.Chrome()

url = 'https://search.jd.com/Search?keyword=%E7%94%B5%E8%84%91&enc=utf-8&wq=dianano&pvid=626a8085bf6346f9af4fe372d3811c78'

chrome.get(url)

js = 'document.documentElement.scrollTop=100000'
chrome.execute_script(js)
sleep(10)
html = chrome.page_source

e = etree.HTML(html)
prices = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-price"]/strong/i/text()')
names = e.xpath('//div[@class="gl-i-wrap"]/div[@class="p-name p-name-type-2"]/a/em')

print(len(names))
for name, price in zip(names, prices):
    print(name.xpath('string(.)'), ':', price)
