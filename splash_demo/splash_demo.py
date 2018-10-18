import requests
from fake_useragent import UserAgent

splash_url = 'http://192.168.99.100:32768/render.html?url={}&wait=1'
url = 'https://www.guazi.com/bj/buy/'
headers = {
    'User-agent': UserAgent().chrome
}
response = requests.get(splash_url.format(url), headers=headers)
response.encoding = 'utf-8'
print(response.text)
