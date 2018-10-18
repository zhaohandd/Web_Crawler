import pymongo

# 连接数据库
client = pymongo.MongoClient()

# 选择实例
person = client.person

# 选择集合
student = person.student

# 操作数据 #
# 查询数据
results = student.find()
for result in results:
    print(result)

print('----------------------------1----------------------------------------')
# 过滤条件
results = student.find({'country':'China'})
for result in results:
    print(result)

print('-----------------------------2---------------------------------------')

# 排序
results = student.find().sort('age', -1)
for result in results:
    print(result)

print('------------------------------3--------------------------------------')

# 偏移（分页）
results = student.find().limit(6).skip(5)
for result in results:
    print(result)

print('------------------------------4--------------------------------------')
# 增加数据(插入)
data = {'name': 'zhao', 'age': 18, 'country': 'USA'}
student.insert_one(data)

print('------------------------------5--------------------------------------')
# 删除数据
data = {'name': 'hanhan', 'age': 20}
student.remove(data)
print('success~')

print('------------------------------6--------------------------------------')
# 修改数据（更新）
data = {'name': 'dawu'}
result = student.find_one(data)
print(result)
result['country'] = 'England'
student.update(data, {'$set': result})
