import abc


class SchoolReport(abc.ABC):

    @abc.abstractmethod
    def report(self):
        pass

    @abc.abstractmethod
    def sign(self):
        pass


class FouthGradeSchoolReport(SchoolReport):

    def report(self):
        print("尊敬的XXX家长")
        print("......")
        print("语文 62 数学 65 体育 98 自然 63")
        print("......")
        print("          家长签名：")

    def sign(self, name):
        print("家长签名为：%s" % name)


class HighScoreDecorator(object):

    def __init__(self, sr):
        self.sr = sr

    def reportHighScore(self):
        print("这次考试语文最高75，数学78，自然80")

    def report(self):
        self.reportHighScore()
        self.sr.report()


class SortDecorator(object):

    def __init__(self, sr):
        self.sr = sr

    def reportSort(self):
        print("我是排名第38名")

    def report(self):
        self.sr.report()
        self.reportSort()


if __name__ == '__main__':
    sr = FouthGradeSchoolReport()
    hsd = HighScoreDecorator(sr)
    sd = SortDecorator(sr)
    hsd.report()
    sd.report()
    sr.sign('老三')