# 选择排序
def selectionSort(myList):
    for i in range(len(myList)-1):
        minIndex = i
        for j in range(i+1, len(myList)):
            if myList[minIndex] > myList[j]:
                minIndex = j
        if minIndex != i:
            myList[i], myList[minIndex] = myList[minIndex], myList[i]
    return myList

# selectionSort([49, 38, 65, 97, 76, 13, 27, 49])