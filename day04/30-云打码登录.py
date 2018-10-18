import requests
from fake_useragent import UserAgent
from day04.YDMHTTPDemo3 import get_code


def get_image():
    img_url = 'http://www.yundama.com/index/captcha'
    response = session.get(img_url, headers=headers)
    with open('yzm1.jpg', 'wb') as f:
        f.write(response.content)
    code = get_code('yzm1.jpg')
    print(code)
    return code


def do_login(code):
    login_url = 'http://www.yundama.com/index/login?'
    f_data = {
        'username': '398707160_pt',
        'password': '123456abc',
        'utype': '1',
        'vcode': code
    }

    response = session.get(login_url, headers=headers, params=f_data)
    print(response.text)


if __name__ == '__main__':
    session = requests.Session()
    index_url = 'http://www.yundama.com/'
    headers = {
        'User-agent': UserAgent().random
    }
    response = session.get(index_url, headers=headers)
    code = get_image()
    do_login(code)
