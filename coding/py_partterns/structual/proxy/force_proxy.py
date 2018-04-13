"""强制代理"""


class GamePlayer(object):
    def __init__(self, _name):
        self.name = _name
        self.proxy = None

    def killBoss(self):
        if self.proxy is None:
            print("请使用指定代理访问")
        else:
            print("%s在打怪" % self.name)

    def login(self, user, password):
        if self.proxy is None:
            print("请使用指定代理访问")
        else:
            print("登录名为%s的用户%s登陆成功" % (user, self.name))

    def upgrade(self):
        if self.proxy is None:
            print("请使用指定代理访问")
        else:
            print("%s又升了一级" % self.name)

    def getProxy(self):
        self.proxy = GamePlayerProxy(self)
        return self.proxy

    def isProxy(self):
        if self.proxy is None:
            return False
        else:
            return True


class GamePlayerProxy(object):

    def __init__(self, player):
        self.gamePlayer = player

    def killBoss(self):
        self.gamePlayer.killBoss()

    def login(self, user, password):
        self.gamePlayer.login(user, password)

    def upgrade(self):
        self.gamePlayer.upgrade()


if __name__ == '__main__':
    print("----直接访问角色----")
    player = GamePlayer("张三")
    print("开始时间：2018-04-13 10:35")
    player.login("zhangsan", "123456")
    player.killBoss()
    player.upgrade()
    print("结束时间：2018-04-15 10:35")
    print("----直接访问代理----")
    player = GamePlayer('张三')
    proxy = GamePlayerProxy(player)
    print("开始时间：2018-04-13 10:35")
    proxy.login("zhangsan", "123456")
    proxy.killBoss()
    proxy.upgrade()
    print("结束时间：2018-04-15 10:35")
    print("----强制代理场景----")
    player = GamePlayer("里斯")
    proxy = player.getProxy()
    print("开始时间：2018-04-13 10:35")
    proxy.login("lisi", "123456")
    proxy.killBoss()
    proxy.upgrade()
    print("结束时间：2018-04-15 10:35")


