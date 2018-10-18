from urllib.request import urlopen
"""
    爬取一个页面的源代码--urllib库
"""
url = 'http://www.baidu.com'

#发送请求
response = urlopen(url)
#读取内容
info = response.read()
#打印内容
print(info.decode())
print('--------------------------------------------------')

#打印状态码
print(response.getcode())
print('--------------------------------------------------')
#打印真是url
print(response.geturl())
print('--------------------------------------------------')
#打印响应头
print(response.info())
