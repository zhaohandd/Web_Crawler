import requests
from fake_useragent import UserAgent
from lxml import etree

url = 'https://tuchong.com/1351605/21387319/'
headers = {
    'User-Agent': UserAgent().chrome
}
response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
img_urls = e.xpath('//img[@class="multi-photo-image"]/@src')
for img_url in img_urls:
    response = requests.get(img_url, headers=headers)
    img_name = img_url[img_url.rfind('/')+1:]
    with open('img/'+img_name, 'wb') as f:
        print('正在打印' + str(img_name))
        f.write(response.content)
