import requests
from fake_useragent import UserAgent
from lxml import etree


# url管理
class URLManager:
    def __init__(self):
        self.new_url = []
        self.old_url = []

    # 获取一个url
    def get_new_url(self):
        url = self.new_url.pop()
        self.old_url.append(url)
        return url

    # 增加一个url
    def add_new_url(self, url):
        if url not in self.new_url and url and self.old_url:
            self.new_url.append(url)

    # 增加多个url
    def add_new_urls(self, urls):
        for url in urls:
            self.add_new_url(url)

    # 判断是否还有可以爬取的url
    def has_new_url(self):
        return self.get_new_url_size()

    # 获取可以爬取的数量
    def get_new_url_size(self):
        return len(self.new_url)

    # 获取已经爬取的数量
    def get_old_url_size(self):
        return len(self.old_url)


# 爬取
class Downloader:
    def download(self, url):
        response = requests.get(url, headers={'User-agent': UserAgent().random})
        if response.status_code == 200:
            response.encoding = 'utf8'
            return response.text
        else:
            return None


# 解析
class Parser:
    def parse(self, html):
        e = etree.HTML(html)
        datas = self.parse_info(e)
        urls = self.parse_urls(e)
        return datas, urls

    def parse_info(self, e):
        spans = e.xpath('//div[@class="content"]/span[1]')
        datas = []
        for span in spans:
            datas.append(span.xpath('string(.)'))
        return datas

    def parse_urls(self, e):
        base_url = 'https://www.qiushibaike.com{}'
        urls = []
        for url in e.xpath('//ul[@class="pagination"]/li/a/@href'):
            urls.append(base_url.format(url))

# 数据处理
class DataOutput:
    def save(self, datas):
        with open('段子.txt', 'a', encoding='utf-8') as f:
            for data in datas:
                f.write(data)


# 调度
class Dispatch:
    def __init__(self):
        self.downloader = Downloader()
        self.url_manager = URLManager()
        self.parser = Parser()
        self.data_saver = DataOutput()

    def run(self, url):
        self.url_manager.add_new_url(url)
        while self.url_manager.has_new_url():
            url = self.url_manager.get_new_url()
            html = self.downloader.download(url)
            datas, urls = self.parser.parse(html)
            self.data_saver.save(datas)
            self.url_manager.add_new_urls(urls)

if __name__ == '__main__':
    dispatch = Dispatch()
    dispatch.run('https://www.qiushibaike.com/text/page/1/')