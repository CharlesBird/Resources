import uuid


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        """唯一序列号"""
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.s = str(uuid.uuid1())
        return cls._instance


if __name__ == '__main__':
    class UniqueSeq(Singleton):
        pass

    us1 = UniqueSeq()
    print(id(us1), us1.s)
    us2 = UniqueSeq()
    print(id(us2), us2.s)