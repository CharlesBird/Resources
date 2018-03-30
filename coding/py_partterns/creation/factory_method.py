"""工厂方法模型"""


class ChinaGetter(object):

    def __init__(self):
        self.trans = {'dog': '狗', 'cat': '猫'}

    def get(self, msgid):
        return self.trans.get(msgid, str(msgid))


class EnglishGetter(object):

    def get(self, msgid):
        return str(msgid)


def get_localizer(language='English'):
    """工厂方法对象"""
    languages = dict(English=EnglishGetter, China=ChinaGetter)
    return languages[language]()


if __name__ == '__main__':
    e, c = get_localizer('English'), get_localizer('China')
    for msgid in 'dog parrot cat bear'.split():
        print(e.get(msgid), c.get(msgid))