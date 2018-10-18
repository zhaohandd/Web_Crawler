import json

str = '{"name": "盗梦空间"}'
print(type(str))

#把Json格式字符串解码转换成Python对象
obj = json.loads(str)
print(type(obj))

#实现python类型转化为json字符串，返回一个str对象
str2 = json.dumps(obj)
print(type(str2))

#将Python内置类型序列化为json对象后写入文件
json.dump(obj, open('movie.txt', 'w', encoding='utf-8'), ensure_ascii=False)

#读取文件中json形式的字符串元素 转化成python类型
str3 = json.load(open('movie.txt', 'r', encoding='utf-8'))
print(str3)
