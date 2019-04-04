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


def is_win(n, N=None):
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


def fn10():
    return [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
def fn9(num, n=9):
    l = [num] * n
    s = num * n
    remain = 100 - s
    l.append(remain)
    return l

def fn8(num, n=8):
    # 循环两次
    l = []
    s = num * n
    remain = 100 - s
    min_val = num + 1
    max_val = remain - (9-n)*num + 1
    for i in range(min_val, max_val):
        if remain - i < i * (9 - n):
            break
        j = remain - i
        if j >= i:
            l.append((i, j))
    return l

def fn7(num, n=7):
    # 循环三次次
    l = []
    s = num * n
    remain = 100 - s
    min_val = num + 1
    max_val = remain - (9-n)*num + 1
    for i in range(min_val, max_val):
        if remain - i < i * (9 - n):
            break
        for j in range(i, max_val):
            if remain - i - j < j * (8 - n):
                break
            k = remain - (i + j)
            if k >= j:
                l.append((i, j, k))
    return l

def fn6(num, n=6):
    # 循环四次
    l = []
    s = num * n
    remain = 100 - s
    min_val = num + 1
    max_val = remain - (9-n)*num + 1
    for i in range(min_val, max_val):
        if remain - i < i * (9 - n):
            break
        for j in range(i, max_val):
            if remain - i - j < j * (8 - n):
                break
            for k in range(j, max_val):
                if remain - i - j - k < k * (7 - n):
                    break
                a = remain - (i + j + k)
                if a >= k:
                    l.append((i, j, k, a))
    return l

def fn5(num, n=5):
    # 循环五次
    l = []
    s = num * n
    remain = 100 - s
    min_val = num + 1
    max_val = remain - (9-n)*num + 1
    for i in range(min_val, max_val):
        if remain - i < i * (9 - n):
            break
        for j in range(i, max_val):
            if remain - i - j < j * (8 - n):
                break
            for k in range(j, max_val):
                if remain - i - j - k < k * (7 - n):
                    break
                for a in range(k, max_val):
                    if remain - i - j - k - a < a * (6 - n):
                        break
                    b = remain - (i + j + k + a)
                    if b >= a:
                        l.append((i, j, k, a, b))
    return l

def fn4(num, n=4):
    # 循环六次
    l = []
    s = num * n
    remain = 100 - s
    min_val = num + 1
    max_val = remain - (9-n)*num + 1
    for i in range(min_val, max_val):
        if remain - i < i * (9 - n):
            break
        for j in range(i, max_val):
            if remain - i - j < j * (8 - n):
                break
            for k in range(j, max_val):
                if remain - i - j - k < k * (7 - n):
                    break
                for a in range(k, max_val):
                    if remain - i - j - k - a < a * (6 - n):
                        break
                    for b in range(a, max_val):
                        if remain - i - j - k - a - b < b * (5 - n):
                            break
                        c = remain - (i + j + k + a + b)
                        if c >= b:
                            l.append((i, j, k, a, b, c))
    return l


def fn3(num, n=3):
    # 循环七次
    l = []
    s = num * n
    remain = 100 - s
    min_val = num + 1
    max_val = remain - (9-n)*num + 1
    for i in range(min_val, max_val):
        if remain - i < i * (9 - n):
            break
        for j in range(i, max_val):
            if remain - i - j < j * (8 - n):
                break
            for k in range(j, max_val):
                if remain - i - j - k < k * (7 - n):
                    break
                for a in range(k, max_val):
                    if remain - i - j - k - a < a * (6 - n):
                        break
                    for b in range(a, max_val):
                        if remain - i - j - k - a - b < b * (5 - n):
                            break
                        for c in range(b, max_val):
                            if remain - i - j - k - a - b - c < c * (4 - n):
                                break
                            x = remain - (i + j + k + a + b + c)
                            if x >= c:
                                l.append((i, j, k, a, b, c, x))
    return l

def fn2(num, n=2):
    # 循环八次
    l = []
    s = num * n
    remain = 100 - s
    min_val = num + 1
    max_val = remain - (9-n)*num + 1
    for i in range(min_val, max_val):
        if remain - i < i * (9 - n):
            break
        for j in range(i, max_val):
            if remain - i - j < j * (8 - n):
                break
            for k in range(j, max_val):
                if remain - i - j - k < k * (7 - n):
                    break
                for a in range(k, max_val):
                    if remain - i - j - k - a < a * (6 - n):
                        break
                    for b in range(a, max_val):
                        if remain - i - j - k - a - b < b * (5 - n):
                            break
                        for c in range(b, max_val):
                            if remain - i - j - k - a - b - c < c * (4 - n):
                                break
                            for x in range(c, max_val):
                                if remain - i - j - k - a - b - c - x < x * (3 - n):
                                    break
                                y = remain - (i + j + k + a + b + c + x)
                                if y >= x:
                                    l.append((i, j, k, a, b, c, x, y))
    return l

def fn1(num, n=1):
    # 循环九次
    l = []
    s = num * n
    remain = 100 - s
    min_val = num + 1
    max_val = remain - (9-n)*num + 1
    for i in range(min_val, max_val):
        if remain - i < i * (9-n):
            break
        for j in range(i, max_val):
            if remain - i - j < j * (8-n):
                break
            for k in range(j, max_val):
                if remain - i - j - k < k * (7-n):
                    break
                for a in range(k, max_val):
                    if remain - i - j - k - a < a * (6-n):
                        break
                    for b in range(a, max_val):
                        if remain - i - j - k - a - b < b * (5-n):
                            break
                        for c in range(b, max_val):
                            if remain - i - j - k - a - b - c < c * (4-n):
                                break
                            for x in range(c, max_val):
                                if remain - i - j - k - a - b - c - x < x * (3-n):
                                    break
                                for y in range(x, max_val):
                                    if remain - i - j - k - a - b - c - x - y < y * (2 - n):
                                        break
                                    z = remain - (i + j + k + a + b + c + x + y)
                                    if z < y:
                                        break
                                    if z >= y:
                                        l.append((i, j, k, a, b, c, x, y, z))
    return l


def get_result():
    # res = [[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]
    yield '10 + 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10'
    for n in range(1, 10):
        fn = 'fn' + str(n)
        for num in range(1, 10):
            if n == 9:
                line = fn9(num)
                yield ' + '.join(map(str, line))
                # res.append(' + '.join(map(str, line)))
            else:
                fn_copy = fn + ('({})'.format(num))
                for l in eval(fn_copy):
                    line = [num] * n
                    line.extend(list(l))
                    yield ' + '.join(map(str, line))
                    # res.append(' + '.join(map(str, line)))


def get_result2():
    res = ['10 + 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10 + 10']
    for n in range(1, 10):
        fn = 'fn' + str(n)
        for num in range(1, 10):
            if n == 9:
                line = fn9(num)
                res.append(' + '.join(map(str, line)))
            else:
                fn_copy = fn + ('({})'.format(num))
                for l in eval(fn_copy):
                    line = [num] * n
                    line.extend(list(l))
                    res.append(' + '.join(map(str, line)))
    return res


# if __name__ == '__main__':
#     f = open('=100.csv', 'w+')
#     ct = 0
#     for ln in get_result():
#         f.write(ln+'\n')
#         ct += 1
#     # print(ct)
#     f.write('Count: ' + str(ct))

s = 'a'

def f():
    global s, a
    print(s)

f()