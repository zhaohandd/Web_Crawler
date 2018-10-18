from urllib.request import urlopen, Request
from fake_useragent import UserAgent
from urllib.error import URLError
"""
    URLError出现的主要原因:
    网络无连接，即本机无法上网
    连接不到特定的服务器
    服务器不存在
"""
url = 'http://www.sxt.cn/index/login/login123'
headers = {
    'User-agent': UserAgent().chrome
}
try:
    request = Request(url, headers=headers)
    response = urlopen(request)
    print(response.read().decode())
except URLError as e:
    if e.args == ():
        print(e.code)
    else:
        print(e.args)
