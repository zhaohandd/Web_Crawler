from urllib.request import urlopen, Request
from fake_useragent import UserAgent
"""
    ajax请求生成的动态页码爬取
    XMLHttpRequest
"""
base_url = 'https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&start={}&limit=200'

i = 0
while True:
    url = base_url.format(i * 20)
    headers = {
        'User-agent': UserAgent().chrome
    }

    request = Request(url, headers=headers)
    response = urlopen(request)
    info = response.read().decode()

    print(info)

    if info == '[]' or info is None:
        break

    i += 1

