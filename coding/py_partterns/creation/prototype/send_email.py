import random
import threading
from copy import deepcopy


class AdvTemplate(object):

    def __init__(self):
        self.advSubject = "XX银行国际信用卡抽奖活动"
        self.advContext = "国庆抽奖活动通知：只要刷卡就送你一百万。"

    def getAdvSubject(self):
        return self.advSubject

    def getadvContext(self):
        return self.advContext


class Mail(object):

    def __init__(self, adv_template):
        self.receiver = None
        self.appellation = None
        self.tail = None
        self.context = adv_template.getAdvSubject()
        self.subject = adv_template.getadvContext()

    def setReceiver(self, receiver):
        self.receiver = receiver

    def setAppellation(self, appellation):
        self.appellation = appellation

    def setTail(self, tail):
        self.tail = tail

    def setContext(self, context):
        self.context = context

    def setSubject(self, subject):
        self.subject = subject

    def clone(self):
        return deepcopy(self)


def get_randstring(n):
    source = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return ''.join(random.sample(source, n))


def send_mail(mail):
    # print("标题：%s\t收件人：%s\t...发送成功！" % (mail.subject, mail.receiver))
    print(mail.receiver, mail.subject, mail.tail, mail.appellation, mail.context)


if __name__ == '__main__':
    import timeit
    def thrend_foo():
        Max_COUNT = 600
        i = 0
        mail = Mail(AdvTemplate())
        mail.setTail("XX银行版权所有")
        while i < Max_COUNT:
            cloneMail = mail.clone()
            cloneMail.setAppellation("%s先生（女士）" % get_randstring(5))
            cloneMail.setReceiver("%s@%s.com" % (get_randstring(5), get_randstring(8)))
            t = threading.Thread(target=send_mail, args=(cloneMail,))
            t.start()
            # send_mail(mail)
            i += 1


    def foo():
        Max_COUNT = 600
        i = 0
        mail = Mail(AdvTemplate())
        mail.setTail("XX银行版权所有")
        while i < Max_COUNT:
            mail.setAppellation("%s先生（女士）" % get_randstring(5))
            mail.setReceiver("%s@%s.com" % (get_randstring(5), get_randstring(8)))
            send_mail(mail)
            i += 1


    t1 = timeit.Timer(thrend_foo)
    t2 = timeit.Timer(foo)
    print(t1.repeat(3, 10000), t2.repeat(3, 10000))