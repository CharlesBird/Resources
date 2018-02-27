import win32gui
import win32api
import win32con
import time
import win32com.client
classname = None
# titlename = "百度一下，你就知道 - Mozilla Firefox"
# titlename = "51沪牌模拟拍牌系统 - Mozilla Firefox"
# titlename = "百度一下，你就知道 - Internet Explorer"
titlename = "51沪牌模拟拍牌系统 - Internet Explorer"
#获取句柄
hwnd = win32gui.FindWindow(classname, titlename)  # 根据名称获取窗口句柄
win32gui.ShowWindow(hwnd, win32con.SW_SHOWMAXIMIZED)  # 窗口最大化
win32gui.SetForegroundWindow(hwnd)  # 展示句柄窗口
# time.sleep(1)
win32gui.MoveWindow(hwnd, 0, 0, 1200, 888, True)  # 设定浏览器大小
#获取窗口左上角和右下角坐标
# left, top, right, bottom = win32gui.GetWindowRect(hwnd)
# print(left, top, right, bottom)
shell = win32com.client.Dispatch("WScript.Shell")
win32api.SetCursorPos([840, 405])  # 加价输入位置
# 双击输入框清除历史数据
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 单击动作
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
win32api.keybd_event(8, 0, 0, 0)  # 触发Backspace按钮
win32api.keybd_event(8, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放点击动作
shell.SendKeys('800')
win32api.SetCursorPos([948, 405])  # 加价按钮位置
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 单击动作
win32api.SetCursorPos([948, 508])  # 出价按钮位置
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 单击动作