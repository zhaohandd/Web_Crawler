import requests
from fake_useragent import UserAgent

#关闭警告
requests.packages.urllib3.disable_warnings()

headers = {
    'User-agent': UserAgent().chrome
}
url = 'https://www.12306.cn/mormhweb/'

response = requests.get(url, verify=False, headers=headers)
response.encoding = 'utf-8'
print(response.text)
