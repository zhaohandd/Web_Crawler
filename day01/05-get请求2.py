from urllib.parse import urlencode
from urllib.request import urlopen, Request

args = {
    'wd': 'fiddle下载',
    'ie': 'utf-8'
}
url = 'https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=1&tn=baidu&{}'.format(urlencode(args))
headers = {
    'User-agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'
}

request = Request(url, headers=headers)
response = urlopen(request)
print(response.read().decode())
