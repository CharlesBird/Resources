import win32gui
import win32api
import win32con
import time
import win32com.client
classname = None
# titlename = "百度一下，你就知道 - Mozilla Firefox"
titlename = "51沪牌模拟拍牌系统"
# titlename = "百度一下，你就知道"
#获取句柄
hwnd = win32gui.FindWindow(classname, titlename)  # 根据名称获取窗口句柄
print(hwnd)
win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)  # 窗口最大化
#获取窗口左上角和右下角坐标
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
print(left, top, right, bottom)
# shell = win32com.client.Dispatch("WScript.Shell")
shell = win32com.client.Dispatch("InternetExplorer.Application")
shell.SendKeys('%')
win32gui.SetForegroundWindow(hwnd)  # 展示句柄窗口
time.sleep(1)
# win32api.SetCursorPos([650, 343])  # 设置鼠标位置
win32api.SetCursorPos([1160, 414])
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)  # 单击动作