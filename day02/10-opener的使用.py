from urllib.request import Request, build_opener, HTTPHandler
from fake_useragent import UserAgent

url = 'http://www.baidu.com'
headers = {
    'User-agent': UserAgent().chrome
}

request = Request(url, headers=headers)
opener = build_opener(HTTPHandler(debuglevel=1))
response = opener.open(request)

print(response.read().decode())