class GamePlayer(object):
    def __init__(self, name):
        self.name = name

    def killBoss(self):
        print("%s在打怪" % self.name)

    def login(self, user, password):
        print("登录名为%s的用户%s登陆成功" % (user, self.name))

    def upgrade(self):
        print("%s又升了一级" % self.name)


class GamePlayerProxy(object):
    def __init__(self, player):
        self.player = player

    def killBoss(self):
        self.player.killBoss()

    def login(self, user, password):
        self.player.login(user, password)

    def upgrade(self):
        self.player.upgrade()


if __name__ == '__main__':
    player = GamePlayer('张三')
    proxy = GamePlayerProxy(player)
    print("开始时间：2018-04-13 10:35")
    proxy.login("zhangsan", "123456")
    proxy.killBoss()
    proxy.upgrade()
    print("结束时间：2018-04-15 10:35")