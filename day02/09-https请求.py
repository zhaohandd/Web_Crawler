from urllib.request import urlopen, Request
from fake_useragent import UserAgent
import ssl

url = 'https://www.12306.cn/mormhweb/'
headers = {
    "User-agent": UserAgent().chrome
}

request = Request(url, headers=headers)
# 忽略SSL安全认证
context = ssl._create_unverified_context()

response = urlopen(request, context=context)
info = response.read().decode()

print(info)