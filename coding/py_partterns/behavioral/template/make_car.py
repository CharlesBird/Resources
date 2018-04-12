import abc


class HummerModel(abc.ABC):

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass

    @abc.abstractmethod
    def alarm(self):
        pass

    @abc.abstractmethod
    def enginBoom(self):
        pass

    def run(self):
        self.start()
        self.enginBoom()
        self.alarm()
        self.stop()


class HummerH1Model(HummerModel):

    def alarm(self):
        print("悍马H1鸣笛。。。。")

    def enginBoom(self):
        print("悍马H1引擎声音是这样的。。。")

    def start(self):
        print("悍马H1发动。。")

    def stop(self):
        print("悍马H1停车")


class HummerH2Model(HummerModel):

    def alarm(self):
        print("悍马H2鸣笛。。。。")

    def enginBoom(self):
        print("悍马H2引擎声音是这样的。。。")

    def start(self):
        print("悍马H2发动。。")

    def stop(self):
        print("悍马H2停车")


if __name__ == '__main__':
    h1 = HummerH1Model()
    h1.run()
    h2 = HummerH2Model()
    h2.run()