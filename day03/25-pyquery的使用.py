from pyquery import PyQuery as pq
from fake_useragent import UserAgent
import requests

url = 'http://www.xicidaili.com/nn/'
headers = {
    'User-agent': UserAgent().random
}

response = requests.get(url, headers=headers)
doc = pq(response.text)

trs = doc('#ip_list tr')
for num in range(1, len(trs)):
    ip = trs.eq(num).find('td').eq(1).text()
    port = trs.eq(num).find('td').eq(2).text()
    type = trs.eq(num).find('td').eq(5).text()
    with open('ip.txt', 'a') as f:
        f.write(ip + '--' + port + '--' + type + '\n\n')