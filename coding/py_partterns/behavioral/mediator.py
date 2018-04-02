"""中介者模式，一个对象封装一组对象相互交互，使得它们耦合松散"""


import time
import random


class TC(object):

    def __init__(self):
        self._tm = None
        self._bProblem = 0

    def setup(self):
        print("Set up the test.")
        time.sleep(0.1)
        self._tm.prepareReporting()

    def execute(self):
        if not self._bProblem:
            print("Executeing the test")
            time.sleep(0.1)
        else:
            print("Problem in setup. Test not executed.")

    def tearDown(self):
        if not self._bProblem:
            print("Tearing down")
            time.sleep(0.1)
            self._tm.publishReport()
        else:
            print("Test not exxcute.Teardown not required.")

    def setTM(self, tm):
        self._tm = tm

    def setProblem(self, value):
        self._bProblem = value


class Reporter(object):

    def __init__(self):
        self._tm = None

    def prepare(self):
        print("Reporter Class is preparing to report the results")
        time.sleep(0.1)

    def report(self):
        print("Reporting the results of Test")
        time.sleep(0.1)

    def setTM(self, tm):
        self._tm = tm


class DB(object):

    def __init__(self):
        self._tm = None

    def insert(self):
        print("Inserting the execution begin status in the Database")
        time.sleep(0.1)
        if random.randrange(1, 4) == 3:
            return -1

    def update(self):
        print("Updating the test results in Database")
        time.sleep(0.1)

    def setTM(self, tm):
        self._tm = tm


class TestManager(object):

    def __init__(self):
        self._reporter = None
        self._db = None
        self._tc = None

    def prepareReporting(self):
        rvalue = self._db.insert()
        if rvalue == -1:
            self._tc.setProblem(1)
            self._reporter.prepare()

    def publishReport(self):
        self._db.update()
        self._reporter.report()

    def setReporter(self, reporter):
        self._reporter = reporter

    def setDB(self, db):
        self._db = db

    def setTC(self, tc):
        self._tc = tc


if __name__ == '__main__':
    reporter = Reporter()
    db = DB()
    tm = TestManager()
    tm.setDB(db)
    tm.setReporter(reporter)
    reporter.setTM(tm)
    db.setTM(tm)
    for i in range(3):
        tc = TC()
        tc.setTM(tm)
        tm.setTC(tc)
        tc.setup()
        tc.execute()
        tc.tearDown()