"""聊天室"""


import abc


class AbstractUser(abc.ABC):

    def __init__(self, mediator):
        self.mediator = mediator


class User(AbstractUser):

    def sendMessage(self, to, content):
        print("%s发消息给%s: %s" % (self.name, to, content))


class AbstractMediator(abc.ABC):

    def __init__(self):
        self.user = User(self)


class Mediator(AbstractMediator):

    def execute(self):
        pass