from urllib.parse import quote
from urllib.request import urlopen, Request

url = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&wd=fiddler{}'.format(quote('下载'))
headers = {
    'User-agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'
}

request = Request(url, headers=headers)
response = urlopen(request)
print(response.read().decode())

