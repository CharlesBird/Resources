class YellowHuman(object):

    def getColor(self):
        print("黄色皮肤")

    def talk(self):
        print("黄种人说双字节")


class BlackHuman(object):

    def getColor(self):
        print("黑色皮肤")

    def talk(self):
        print("黑种人说话，一般人听不懂")


class WhiteHuman(object):

    def getColor(self):
        print("白色皮肤")

    def talk(self):
        print("白种人说单字节")


class HumanFactory(object):
    def createHuman(self, human='yellow'):
        humans = dict(yellow=YellowHuman, black=BlackHuman, white=WhiteHuman)
        return humans[human]()


if __name__ == '__main__':
    Yinyanglu = HumanFactory()
    yellowHuman = Yinyanglu.createHuman('yellow')
    yellowHuman.getColor()
    yellowHuman.talk()
    blackHuman = Yinyanglu.createHuman('black')
    blackHuman.getColor()
    blackHuman.talk()
    whiteHuman = Yinyanglu.createHuman('white')
    whiteHuman.getColor()
    whiteHuman.talk()