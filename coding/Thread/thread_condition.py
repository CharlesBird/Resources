import threading


class XiaoAi(threading.Thread):

    def __init__(self, con):
        super(XiaoAi, self).__init__(name="小爱")
        self.con = con

    def run(self):
        with self.con:
            self.con.wait()
            print("{}: 在".format(self.name))
            self.con.notify()

            self.con.wait()
            print("{}: 好呀".format(self.name))
            self.con.notify()

            self.con.wait()
            print("{}: 2".format(self.name))
            self.con.notify()

            self.con.wait()
            print("{}: 4".format(self.name))
            self.con.notify()

            self.con.wait()
            print("{}: 7".format(self.name))
            self.con.notify()


class TianMao(threading.Thread):

    def __init__(self, con):
        super().__init__(name="天猫")
        self.con = con

    def run(self):
        with self.con:
            print("{}: 小爱同学".format(self.name))
            self.con.notify()
            self.con.wait()

            print("{}: 考你算法".format(self.name))
            self.con.notify()
            self.con.wait()

            print("{}: 1+1".format(self.name))
            self.con.notify()
            self.con.wait()

            print("{}: 2+2".format(self.name))
            self.con.notify()
            self.con.wait()

            print("{}: 3+4".format(self.name))
            self.con.notify()
            self.con.wait()


if __name__ == '__main__':
    con = threading.Condition()
    xiaoai = XiaoAi(con)
    tianmao = TianMao(con)

    xiaoai.start()
    tianmao.start()
