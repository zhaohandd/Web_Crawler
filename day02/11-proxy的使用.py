from urllib.request import Request, build_opener, ProxyHandler
from fake_useragent import UserAgent

url = 'http://httpbin.org/get'
headers = {
    'User-agent': UserAgent().chrome
}

request = Request(url, headers=headers)
handler = ProxyHandler({'http': '183.245.99.52:80'})
opener = build_opener(handler)
response = opener.open(request)

print(response.read().decode())