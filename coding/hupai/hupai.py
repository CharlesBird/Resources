import win32gui
import win32api
import win32con
import time
import win32com.client


def pos_moseevent(pos=None):
    """定位单击"""
    if not pos:
        raise
    win32api.SetCursorPos(pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


def pos_double_moseevent(pos=None):
    """定位双击"""
    if not pos:
        raise
    win32api.SetCursorPos(pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


def clear_input():
    """清除历史值"""
    win32api.keybd_event(8, 0, 0, 0)  # 触发Backspace按钮
    win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放点击动作

class AtoPP(object):
    def __init__(self, classname, titlename, first_price, second_price=None, advance=100, force_time=57, has_second=False):
        """根据名称获取句柄"""
        self.hwnd = win32gui.FindWindow(classname, titlename)
        self.first_price = first_price
        self.second_price = second_price
        self.advance = advance
        self.force_time = force_time
        self.has_second = has_second

    def show_and_fix_hwnd(self, left=0, top=0, right=1200, bottom=888):
        """展示固定大小句柄，为寻找位置提供帮助"""
        win32gui.ShowWindow(self.hwnd, win32con.SW_SHOWMAXIMIZED)  # 窗口最大化
        win32gui.SetForegroundWindow(self.hwnd)  # 展示句柄窗口
        win32gui.MoveWindow(self.hwnd, left, top, right, bottom, True)  # 设定浏览器大小

    def input_price(self, price):
        """输入加价价格"""
        if not price:
            raise
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys(price)

    def run(self):
        """启动程序"""
        self.show_and_fix_hwnd()
        pos_double_moseevent([840, 405])
        clear_input()
        self.input_price(self.first_price)
        pos_moseevent([948, 405])
        pos_moseevent([948, 508])


if __name__ == '__main__':
    ap = AtoPP(None, '51沪牌模拟拍牌系统 - Internet Explorer', 800)
    ap.run()