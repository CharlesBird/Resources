# 希尔排序
def shellSort(myList):
    list_len = len(myList)
    dk = list_len // 2
    while dk >= 1:
        for i in range(dk, list_len):
            preIndex = i - dk
            current = myList[i]
            while preIndex >= 0 and myList[preIndex] > current:
                myList[preIndex+dk] = myList[preIndex]
                preIndex -= dk
            myList[preIndex+dk] = current
        dk = dk // 2
    print(myList)
    return myList

# shellSort([49, 38, 65, 97, 76, 13, 27, 49])
# shellSort([49, 38, 65, 97, 76, 13, 27, 49, 50, 43])
shellSort([49, 38, 65, 97, 76, 13, 27, 49, 38, 65, 97, 76, 13, 27, 49, 50, 43, 45])