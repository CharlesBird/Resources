# 计数排序,只适用整数，最小值与最大值过大时不适用
def countingSort(myList):
    max_v, min_v = max(myList), min(myList)
    lenth = max_v-min_v + 1
    countList = [0 for _ in range(lenth)]
    res = [None] * len(myList)
    for v in myList:
        countList[v-min_v] += 1
    for i in range(1, lenth):
        countList[i] = countList[i] + countList[i-1]
    for v in myList:
        res[countList[v-min_v] - 1] = v
        countList[v-min_v] -= 1
    return res


countingSort([-49,38,65,97,76,13,27,49])
