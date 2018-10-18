from jsonpath import jsonpath
import requests
from fake_useragent import UserAgent
import json

url = 'http://www.lagou.com/lbs/getAllCitySearchLabels.json'
headers = {
    'User-agent': UserAgent().random
}

response = requests.get(url, headers)
names = jsonpath(json.loads(response.text), '$..name')
codes = jsonpath(response.json(), '$..code')

for name, code in zip(names, codes):
    print(name + '--' + code)
