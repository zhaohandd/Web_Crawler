import requests
from fake_useragent import UserAgent
from lxml import etree
import pymysql

url = 'http://datachart.500.com/ssq/'
headers = {
    'UserAgent': UserAgent().chrome
}

# 提取数据
response = requests.get(url, headers=headers)
e = etree.HTML(response.text)
date_times = e.xpath('//tbody[@id="tdata"]/tr/td[1]/text()')
trs = e.xpath('//tbody[@id="tdata"]/tr[not(@class)]')

# 连接数据库
client = pymysql.connect(host='localhost',
                         port=3306,
                         user='root',
                         password='104715',
                         charset='utf8',
                         db='ball')
cursor = client.cursor()
# 插入数据
sql = 'insert into t_ball values (0, %s, %s, %s)'
# 查看数据是否存在
select_new_sql = 'select * from t_ball where date_time = %s'

date_times.reverse()
# 记录有多少条新数据
index = 0
for date_time in date_times:
    result = cursor.execute(select_new_sql, [date_time])
    if result == 1:
        break
    index += 1
print(index)

trs.reverse()

for i in range(index):
    red_ball = '  '.join(trs[i].xpath('./td[@class="chartBall01"]/text()'))
    blue_ball = trs[i].xpath('./td[@class="chartBall02"]/text()')[0]
    print('第' + date_times[i] + '期：'+ '红球是' + red_ball + '蓝球是' + blue_ball)
    cursor.execute(sql, [date_times[i], red_ball, blue_ball])
    client.commit()

# for date_time, tr in zip(date_times, trs):
#     red_ball = '  '.join(tr.xpath('./td[@class="chartBall01"]/text()'))
#     blue_ball = tr.xpath('./td[@class="chartBall02"]/text()')[0]
#     print('第' + date_time + '期：'+ '红球是' + red_ball + '蓝球是' + blue_ball)
#     cursor.execute(sql, [date_time, red_ball, blue_ball])
#     client.commit()

cursor.close()
client.close()


