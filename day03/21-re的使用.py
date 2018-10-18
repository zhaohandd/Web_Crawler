import re

str1 = 'I Study Python3.6 Everyday'

print('------------match()--------------------')

match1 = re.match(r'I', str1)
match2 = re.match(r'\w', str1)
match3 = re.match(r'.', str1)
match4 = re.match(r'\D', str1)
match5 = re.match(r'\S', str1)

#匹配不到，因为match是从左往右开始匹配的
#match6 = re.match(r'Study', str1)

print(match1.group())
print(match2.group())
print(match3.group())
print(match4.group())
print(match5.group())

print('------------search()--------------------')

search1 = re.search(r'Study', str1)
search2 = re.search(r'S\w+', str1)
search3 = re.search(r'P\w+.\d', str1)
print(search1.group())
print(search2.group())
print(search3.group())

print('--------------findall()------------------')
findall1 = re.findall(r'y', str1)
print(findall1)

print('--------------test()------------------')
str2 = '<div><a href="http://www.bjsxt.com">尚学堂bjsxt</a></div>'
t1 = re.findall(r'[\u4e00-\u9fa5]\w+', str2)
t2 = re.findall(r'<a href="http://www.bjsxt.com">(.+)</a>', str2)
t3 = re.findall(r'<a href="(.+)">', str2)

print(t1)
print(t2)
print(t3)

print('--------------sub()------------------')
sub1 = re.sub(r'<div>(.+)</div>', r'<span>\1</span>', str2)
print(sub1)
