# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from pymysql import connect


class RoomPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        self.client.room.lianjia.insert(item)
        return item

    def close_spider(self, spider):
        self.client.close()


class MysqlPipeline(object):
    def open_spider(self, spider):
        self.client = connect(host='localhost', port=3306, user='root', password='root', db='room', charset='utf8')
        self.cursor = self.client.cursor()

    def process_item(self, item, spider):
        args = [
            item['money'],
            item['unitPriceValue']
        ]
        sql = 'INSERT INTO t_lianjia VALUES (0, %s, %s)'
        self.cursor.execute(sql, args)
        self.client.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.client.close()