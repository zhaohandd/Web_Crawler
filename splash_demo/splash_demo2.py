import requests
from fake_useragent import UserAgent

url = 'https://www.guazi.com/bj/buy/'
lua_script = '''
function main(splash, args)
    splash:go('{}')
    splash:wait(1)
    return splash:html()
end
'''.format(url)

splash_url = 'http://192.168.99.100:32768/execute?lua_source={}'.format(lua_script)

headers = {
    'User-agent': UserAgent().chrome
}
response = requests.get(splash_url, headers=headers)
response.encoding = 'utf-8'
print(response.text)
