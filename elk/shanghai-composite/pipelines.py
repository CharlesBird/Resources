import pymongo


class MongoPipeline(object):

    def __init__(self, host, port, mongo_db, coll, user, pwd):
        self.host = host
        self.port = port
        self.mongo_db = mongo_db
        self.coll = coll
        self.user = user
        self.pwd = pwd

    def process_item(self, items):
        """
        批量插入
        :param items: 列表套字典
        :return:
        """
        with pymongo.MongoClient(host=self.host, port=self.port) as client:
            db = client[self.mongo_db]
            db.authenticate(self.user, self.pwd)
            db[self.coll].insert_many(items, ordered=True)