import redis
import json
import pymongo

redis_client = redis.Redis(host='127.0.0.1', port=6379, db=0)
mongo_client = pymongo.MongoClient()

collection = mongo_client.duanzi.qiushi

while True:
    key, data = redis_client.blpop(['qiushi:items'])
    collection.insert(json.loads(data))
    # print(key)
    # print(json.loads(data))