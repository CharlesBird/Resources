# 插入排序
def insertionSort(myList):
    for i in range(len(myList)):
        preIndex = i - 1
        current = myList[i]
        while preIndex >= 0 and myList[preIndex] > current:
            myList[preIndex+1] = myList[preIndex]
            preIndex -= 1
        myList[preIndex+1] = current
    return myList

# insertionSort([49, 38, 65, 97, 76, 13, 27, 49])