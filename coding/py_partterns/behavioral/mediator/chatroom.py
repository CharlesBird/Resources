"""聊天室"""


import abc


class AbstractUser(abc.ABC):

    def __init__(self, mediator):
        self.mediator = mediator


class User(AbstractUser):

    def __init__(self, name, mediator):
        self.name = name
        self.mediator = mediator

    def sendMessage(self, content):
        self.mediator.sendMessage(content, self)

    def getNotify(self, content):
        print("%s得到对方消息%s" % (self.name, content))


class AbstractMediator(abc.ABC):

    def __init__(self, name):
        self.name = name


class Mediator(AbstractMediator):

    user1 = None
    user2 = None

    def sendMessage(self, content, user):
        if user == self.user1:
            self.user2.getNotify(content)
        else:
            self.user1.getNotify(content)


if __name__ == '__main__':
    mediator = Mediator('聊天室')
    zs = User('张三', mediator)
    mediator.user1 = zs
    ls = User('里斯', mediator)
    mediator.user2 = ls

    zs.sendMessage('里斯你是外国人吗')
    ls.sendMessage('我不是外国人')