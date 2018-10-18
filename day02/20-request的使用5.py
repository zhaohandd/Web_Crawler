import requests
from fake_useragent import UserAgent
#开启session,保存cookie
session = requests.Session()
#关闭警告
requests.packages.urllib3.disable_warnings()

headers = {
    'User-agent': UserAgent().chrome
}
login_url = 'http://www.sxt.cn/index/login/login'

params = {
    'user': '17703181473',
    'password': '123456'
}

response = session.post(login_url, data=params, headers=headers)

info_url = 'http://www.sxt.cn/index/user.html'

resp = session.get(info_url, headers=headers)

print(resp.text)
