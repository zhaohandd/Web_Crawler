import requests
from fake_useragent import UserAgent
import re

url = 'https://www.qiushibaike.com/text/'
headers = {
    'User-agent': UserAgent().random
}

response = requests.get(url, headers)
info = response.text

infos = re.findall(r'<div class="content">\s*<span>\s*(.+)\s*</span>', info)
with open('段子.txt', 'w', encoding='utf-8') as f:
    for info in infos:
        f.write(info + '\n\n')