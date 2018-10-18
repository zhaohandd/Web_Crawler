import requests
from fake_useragent import UserAgent

headers = {
    'User-agent': UserAgent().chrome
}
url = 'https://www.baidu.com/s'
params = {
    'wd': '尚学堂'
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
