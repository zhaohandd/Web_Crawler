from random import choice
from urllib.request import urlopen, Request
"""
    User Agent中文名为用户代理，是Http协议中的一部分，属于头域的组成部分，User Agent也简称UA。
    它是一个特殊字符串头，是一种向访问网站提供你所使用的浏览器类型及版本、操作系统及版本、浏览器内核、等信息的标识。
    通过这个标识，用户所访问的网站可以显示不同的排版从而为用户提供更好的体验或者进行信息统计；
    例如用手机访问谷歌和电脑访问是不一样的,这些是谷歌根据访问者的UA来判断的。
    UA可以进行伪装。
"""
url = 'http://www.baidu.com'

user_agents = ['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
              'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
              'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11']
headers = {
    'User-agent': choice(user_agents)
}
request = Request(url, headers=headers)
print(request.get_header('User-agent'))

response = urlopen(request)

info = response.read()

print(info.decode())