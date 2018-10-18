from bs4 import BeautifulSoup, Comment

str = '''
<title id='title'>尚学堂</title>
<div class='info' float='left'>Welcome to SXT</div>
<div class='info' float='right'>
    <span>Good Good Study</span>
    <a href='www.bjsxt.cn'></a>
    <strong><!--没用--></strong>
</div>
'''

soup = BeautifulSoup(str, 'lxml')

#获取属性
print(soup.div.attrs)
print(soup.div.get('class'))
print(soup.div['class'])
print(soup.a['href'])

#获取内容
print(soup.div.string)
print(soup.div.text)

#获取注释
if type(soup.strong.string) == Comment:
    print(soup.strong.prettify())
else:
    print(soup.strong.string)

#过滤器
print(soup.find_all('title'))
print(soup.find_all(id = 'title'))
print(soup.find_all(class_ = 'info'))
print(soup.find_all('div', attrs = {'float': 'left'}))

#CSS选择器
print(soup.select('title'))
print(soup.select('#title'))
print(soup.select('div span'))
print(soup.select('div > span'))
print(soup.select('div')[1].select('a'))
