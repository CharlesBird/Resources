"""普通代理模式"""


class GamePlayer(object):
    def __init__(self, _ganmeplayer, _name):
        if _ganmeplayer is None:
            raise Exception("不能创建正式角色")
        self.name = _name

    def killBoss(self):
        print("%s在打怪" % self.name)

    def login(self, user, password):
        print("登录名为%s的用户%s登陆成功" % (user, self.name))

    def upgrade(self):
        print("%s又升了一级" % self.name)


class GamePlayerProxy(object):

    def __init__(self, name):
        self.gamePlayer = GamePlayer(self, name)

    def killBoss(self):
        self.gamePlayer.killBoss()

    def login(self, user, password):
        self.gamePlayer.login(user, password)

    def upgrade(self):
        self.gamePlayer.upgrade()


if __name__ == '__main__':
    proxy = GamePlayerProxy('张三')
    print("开始时间：2018-04-13 10:35")
    proxy.login("zhangsan", "123456")
    proxy.killBoss()
    proxy.upgrade()
    print("结束时间：2018-04-15 10:35")