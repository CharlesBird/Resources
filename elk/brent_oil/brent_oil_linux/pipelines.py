import pymongo
import threading
import logging
_logger = logging.getLogger(__name__)


class MongoPipeline(object):

    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        """
        线程安全单例模式
        :param args:
        :param kwargs:
        :return:
        """
        cls._lock.acquire()
        if not cls._instance:
            cls._instance = super(MongoPipeline, cls).__new__(cls)
        cls._lock.release()
        return cls._instance

    def __init__(self, host, port, mongo_db, user, pwd, coll):
        self.host = host
        self.port = int(port)
        self.mongo_db = mongo_db
        self.coll = coll
        self.user = user
        self.pwd = pwd

    def process_item(self, item):
        """
       插入
        :param item: 字典
        :return:
        """
        with pymongo.MongoClient(host=self.host, port=self.port) as client:
            db = client[self.mongo_db]
            db.authenticate(self.user, self.pwd)
            db[self.coll].update({'now_time': item["now_time"]}, {'$set': item}, True)

    def process_items(self, items):
        """
        批量插入
        :param items: 列表套字典
        :return:
        """
        with pymongo.MongoClient(host=self.host, port=self.port) as client:
            db = client[self.mongo_db]
            db.authenticate(self.user, self.pwd)
            db[self.coll].insert(items)
            _logger.debug('Insert items succesfully.')
            _logger.debug('items: %s' % items)