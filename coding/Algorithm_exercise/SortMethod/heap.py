# 堆排序
import math
# 画树形结构
def printTree(myList):
    index = 1
    depth = math.ceil(math.log2(len(myList)))  # 因为补0了，不然应该是math.ceil(math.log2(len(array)+1))
    sep = '  '
    for i in range(depth):
        offset = 2 ** i
        print(sep * (2 ** (depth - i - 1) - 1), end='')
        line = myList[index:index + offset]
        for j, x in enumerate(line):
            print("{:>{}}".format(x, len(sep)), end='')
            interval = 0 if i == 0 else 2 ** (depth - i) - 1
            if j < len(line) - 1:
                print(sep * interval, end='')
        index += offset
        print()
# printTree([0, 30, 20])
# printTree([0, 30, 20, 80, 40, 50, 10, 60, 70, 90, 22])
# printTree([0, 30, 20, 80, 40, 50, 10, 60, 70, 90, 22, 33, 44, 55, 66, 77, 88, 99, 11])

def heapSort(myList):
    L_len = len(myList)
    parentIndex = L_len // 2
    # 将原始序列构造成一个大顶堆
    # 遍历从中间开始，到0结束，其实这些都是堆的分支节点
    while parentIndex >= 0:
        heapAdjust(myList, parentIndex, L_len-1)
        parentIndex -= 1
    endIndex = L_len - 1
    # 逆序遍历整个序列，不断取出根节点的值，
    while endIndex > 0:
        # 将当前根节点，也就是列表最开头，下标为0的值，交换到最后面endIndex处
        myList[0], myList[endIndex] = myList[endIndex], myList[0]
        # 将发生变化的序列重新构造成大顶堆
        heapAdjust(myList, 0, endIndex-1)
        endIndex -= 1
    return myList

def heapAdjust(myList, start, end):
    """
    核心的大顶堆构造方法
    当前节点的左子节点索引=2 * start
    当前节点的右子节点索引=2 * start + 1
    """
    temp = myList[start]
    childIndex = 2 * start
    while childIndex <= end:
        if childIndex < end and myList[childIndex] < myList[childIndex+1]:
            childIndex += 1
        if temp >= myList[childIndex]:
            break
        myList[start] = myList[childIndex]
        start = childIndex
        childIndex *= 2
    myList[start] = temp

# heapSort([30, 20, 80, 40, 50, 10, 60, 70, 90, 22])