class User(object):

    def get_info(self):
        print("获取内部员工信息")


class OtherUser(object):

    def get_user(self):
        print("某系统员工信息")


class Adapter(object):

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def get_info(self):
        self.adaptee.get_user()


if __name__ == '__main__':
    u = User()
    ou = Adapter(OtherUser())
    objects = [u, ou]
    for o in objects:
        o.get_info()