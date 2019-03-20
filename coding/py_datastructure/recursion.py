"""递归算法"""


def recursion(n):
    """递归实现n的阶乘"""
    if n == 1:
        return n
    return n * recursion(n-1)


# l =[1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15,[16,[17,]],19]]]]]]]
l = [1, [2, 3], 4, [[5, 6, [7, 8]], [9, 10]]]

def search(l):
    for item in l:
        if type(item) is list:
            search(item)
        else:
            print(item)

line = [1,2,3,4,5,6]
def howmanyin(lst):
    print(lst)
    if lst[1:]:
        print('me and the guys behind')
        tmp = howmanyin(lst[1:])
        print(tmp)
        return 1+tmp
    else:
        print('just me')
        return 1

if __name__ == '__main__':
    print(howmanyin(line))
    # print(recursion(5))
    # search(l)
