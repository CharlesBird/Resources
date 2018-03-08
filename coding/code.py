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


def re_xmltag(x):
    """验证xml标签有效"""
    p = re.compile(r'</?[a-z]+>')
    l = p.findall(x)
    n = len(l)
    if n % 2:
        return False
    for i in range(n//2):
        tag1 = l[i]
        tag2 = l[n-i-1]
        if tag1[1:] != tag2[2:]:
            return False
    return True

# print(re_xmltag('<a></a>'))
# print(re_xmltag('<a></b>'))


def is_win(n, N=N):
    """#棋判断输赢"""
    win1 = ['x'] * N
    win2 = ['o'] * N
    board = [['-' for _ in range(N)] for _ in range(N)]  # Building an empty chessboard
    # Replace the value on the chessboard
    for row in range(len(n)):
        for col in range(len(n[row])):
            board[row][col] = n[row][col]
    all_l = []
    cols_l = get_cols(board)
    all_l.extend(cols_l)
    rows_l = get_rows(board)
    all_l.extend(rows_l)
    diagonals_l = get_diagonals(board, N)
    all_l.extend(diagonals_l)  # merge all list
    if win1 in all_l or win2 in all_l:
        # if anyone in all list, return true
        return True
    return False


def get_rows(board):
    """All rows list"""
    return board

def get_cols(board):
    """All cols list"""
    return list(map(list, zip(*board)))

def get_diagonals(board, N):
    """All diagonals list"""
    diagonal1 = []
    for i in range(N):
        diagonal1.append(board[i][i])
    diagonal2 = []
    for j in range(N):
        diagonal2.append(board[j][N-j-1])
    return [diagonal1, diagonal2]

# print(is_win([['o'], ['x', 'x', 'o'], ['o']], N=3))
# print(is_win([['o'], ['x', 'x', 'x'], ['o']], N=3))
# print(is_win([['o'], ['x', 'x', 'x']], N=3))
# print(is_win([['o', 'x'], ['x', 'x'], ['o', 'x']], N=3))