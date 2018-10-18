import requests
from fake_useragent import UserAgent

headers = {
    'User-agent': UserAgent().chrome
}
url = 'http://httpbin.org/get'
proxies = {
    'http': '',
}
response = requests.get(url, headers=headers, proxies=proxies)

print(response.text)
