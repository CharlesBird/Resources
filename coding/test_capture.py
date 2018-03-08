from PIL import ImageGrab

im = ImageGrab.grab((276, 485, 343, 500))  # 截图系统时间

# im = ImageGrab.grab((304, 500, 348, 515))  # 截图最低成交价

im.save('D:\github\coding\hha.jpg')