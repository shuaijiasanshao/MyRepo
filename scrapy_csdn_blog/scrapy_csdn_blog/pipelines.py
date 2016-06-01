# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import pymongo

# 存储到文件
class JsonWriterPipeline(object):

    def __init__(self):
        self.file = codecs.open('../data/blog', mode='w', encoding='utf-8')
  
    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))
        return item

# 存储到Mongodb
class MongodbWriterPipeline(object):

    def __init__(self, host='localhost', port=27017, db_name='mydb', collection_name='blog'):
        client = pymongo.MongoClient(host, port)
        db = client[db_name]
        self.collection = db[collection_name]
    
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
        