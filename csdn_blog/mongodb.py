import pymongo


class Mongodb(object):
    """docstring for Mongodb"""
    def __init__(self, host, port, db_name, collection_name):
        super(Mongodb, self).__init__()
        self.db_name = db_name
        self.collection_name = collection_name
        self.host = host
        self.port = port

    def _get_connection(self):
        return pymongo.MongoClient(self.host, self.port)

    def _get_database(self):
        connection = self._get_connection()
        return connection[self.db_name]

    def _get_collection(self):
        db = self._get_database()
        return db[self.collection_name]

    def insert_data(self, new_document):
        coll = self._get_collection()
        coll.insert(new_document)

    def delete_data(self, condition=None,):
        coll = self._get_collection()
        coll.remove(condition)

    def update_data(self, condition, new_document):
        coll = self._get_collection()
        coll.update(condition, {'$set': new_document})

    def query_data(self, condition=None):
        coll = self._get_collection()
        return coll.find(condition)
