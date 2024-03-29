"""命令模式"""


import os
import time


class MoveFileCommand(object):

    def __init__(self, src, dest):
        self.src = src
        self.dest = dest

    def execute(self):
        self()

    def __call__(self):
        print("renaming {} to {}".format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        print("renaming {} to {}".format(self.dest, self.src))
        os.rename(self.dest, self.src)


if __name__ == '__main__':
    command_stack = []
    command_stack.append(MoveFileCommand('foo.txt', 'bar.txt'))
    command_stack.append(MoveFileCommand('bar.txt', 'baz.txt'))
    for c in command_stack:
        c.execute()
    time.sleep(2)

    for c in reversed(command_stack):
        c.undo()