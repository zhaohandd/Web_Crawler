from urllib.request import Request
from fake_useragent import UserAgent
from urllib.parse import urlencode
from urllib.request import HTTPCookieProcessor, build_opener

#登录
login_url = 'http://www.sxt.cn/index/login/login'
headers = {
    'User-agent': UserAgent().chrome
}
form_data = {
    'user': '17703181473',
    'password': '123456'
}
form_data = urlencode(form_data).encode()
request = Request(login_url, headers=headers, data=form_data)
#response = urlopen(request) 错误的
processor = HTTPCookieProcessor()
opener = build_opener(processor)
response = opener.open(request)
print(response.read().decode())

#访问页面
info_url = 'http://www.sxt.cn/index/user.html'
request = Request(info_url, headers=headers)
#response = urlopen(request)
response = opener.open(request)
print(response.read().decode())