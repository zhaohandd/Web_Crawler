from urllib.request import urlopen, Request
from urllib.parse import urlencode
from fake_useragent import UserAgent


def get_html(url):
    headers = {
        'User-agent': UserAgent().chrome
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    return response.read()


def save_html(filename, html_bytes):
    with open(filename, 'wb') as f:
        f.write(html_bytes)


def main():
    base_url = 'https://tieba.baidu.com/f?&ie=utf-8&{}'
    content = input("请输入下载内容：")
    num = input("请输入下载页数：")
    for pn in range(int(num)):
        args = {
            'kw': content,
            'pn': pn * 50
        }
        args = urlencode(args)
        html_bytes = get_html(base_url.format(args))
        filename = '第' + str(pn + 1) + '页.html'
        print('正在下载' + filename)
        save_html(filename, html_bytes)


if __name__ == '__main__':
    main()