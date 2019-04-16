# 归并排序
def mergeSort(myList):
    if len(myList) <= 1:
        return myList
    mid = len(myList) // 2
    left = myList[:mid]
    right = myList[mid:]
    return merge(mergeSort(left), mergeSort(right))


def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res.extend(left)
    else:
        res.extend(right)
    print(res)
    return res


mergeSort([49,38,65,97,76,13,27,49])