import os

# 列出给定文件下所有文件树形结构
def printFile(path, level):
    if os.path.exists(path):
        files = os.listdir(path)
        for f in files:
            subpath = os.path.join(path, f)
            if os.path.isfile(subpath):
                print ' ' * level + '- ' + os.path.basename(subpath)
            else:
                leveli = level + 1
                print ' ' * level + '- ' + os.path.basename(subpath)
                printFile(subpath, leveli)
if __name__ == '__main__':
    printFile(r'C:', 1)

# 判断一个字符不少于50字，去除空格换行符
len(field_value.replace(' ', '').replace('\n', '')) < 50