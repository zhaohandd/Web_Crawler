from lxml import etree
import requests
from fake_useragent import UserAgent

url = 'https://www.qidian.com/rank/yuepiao?chn=1'
headers = {
    'User-agent': UserAgent().random
}
response = requests.get(url, headers= headers)

e = etree.HTML(response.text)
names = e.xpath('//h4/a/text()')
authors = e.xpath('//p[@class="author"]/a[1]/text()')

print(names)
print(authors)

for num in range(len(names)):
    print(names[num], ':', authors[num])

for name, author in zip(names, authors):
    print(name + '-->' + author)
