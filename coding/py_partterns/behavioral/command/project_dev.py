import abc


class Group(abc.ABC):

    @abc.abstractmethod
    def find(self):
        pass

    @abc.abstractmethod
    def add(self):
        pass

    @abc.abstractmethod
    def delete(self):
        pass

    @abc.abstractmethod
    def change(self):
        pass

    @abc.abstractmethod
    def plan(self):
        pass


class RequirementGroup(Group):

    def find(self):
        print("找到需求组")

    def add(self):
        print("客户要求增加一项需求")

    def change(self):
        print("客户要求修改一项需求")

    def delete(self):
        print("客户要求删除一项需求")

    def plan(self):
        print("客户要求需求变更计划")


class PageGroup(Group):

    def find(self):
        print("找到美工组")

    def add(self):
        print("客户要求增加一个页面")

    def change(self):
        print("客户要求修改一个页面")

    def delete(self):
        print("客户要求删除一个页面")

    def plan(self):
        print("客户要求页面变更计划")


class CodeGroup(Group):

    def find(self):
        print("找到代码组")

    def add(self):
        print("客户要求增加一项功能")

    def change(self):
        print("客户要求修改一项功能")

    def delete(self):
        print("客户要求删除一项功能")

    def plan(self):
        print("客户要求代码变更计划")


class Command(abc.ABC):
    def __init__(self):
        self.rg = RequirementGroup()
        self.pg = PageGroup()
        self.cg = CodeGroup()

    @abc.abstractmethod
    def execute(self):
        pass


class AddRequirementCommand(Command):

    def execute(self):
        self.rg.find()
        self.rg.add()
        self.rg.plan()


class DeletePageCommand(Command):

    def execute(self):
        self.pg.find()
        self.pg.delete()
        self.pg.plan()


class Invoker(object):

    def setCommand(self, command):
        self.command = command

    def action(self):
        self.command.execute()


if __name__ == '__main__':
    xiaosan = Invoker()
    print("------客户要求增加一项需求-------")
    command = AddRequirementCommand()
    xiaosan.setCommand(command)
    xiaosan.action()