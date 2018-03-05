# -*- coding: utf-8 -*-
import os

# 列出给定文件下所有文件树形结构
# def printFile(path, level):
#     if os.path.exists(path):
#         files = os.listdir(path)
#         for f in files:
#             subpath = os.path.join(path, f)
#             if os.path.isfile(subpath):
#                 print(' ' * level + '- ' + os.path.basename(subpath))
#             else:
#                 leveli = level + 1
#                 print(' ' * level + '- ' + os.path.basename(subpath))
#                 printFile(subpath, leveli)
# if __name__ == '__main__':
#     printFile(r'C:', 1)

# 判断一个字符不少于50字，去除空格换行符
# len(field_value.replace(' ', '').replace('\n', '')) < 50


import re

def longest_substring(s):
    n = len(set(s))
    if n == 1:
        return s[0], n
    n = re.findall(r"(\w)(\1+)", s)
    for tp in n:
        s = s.replace(''.join(tp), ',')
    l = s.split(',')
    longest = 0
    subs = ''
    for res in map(lambda x: ''.join(list(set(x))), l):
        if longest < len(res):
            longest = len(res)
            subs = res
        else:
            continue
    return subs, longest

# print(longest_substring('abcabcbb'))
# print(longest_substring('pwwkew'))
# print(longest_substring('bbbbbb'))


def distinct_numbers(s):
    l = s.split('->')
    l2 = list(set(l))
    new_l = []
    for i in l2:
        print(l.count(i), i)
        if l.count(i) == 1:
            new_l.append(i)
    return ('->'.join(map(str, (sorted(map(int, new_l))))))

# print(distinct_numbers('1->1->1->2->3'))
