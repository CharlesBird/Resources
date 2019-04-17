# 冒泡排序
def bubbleSort(myList):
    for i in range(1, len(myList)):
        for j in range(len(myList)-i):
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]
    return myList

# bubbleSort([49,38,65,97,76,13,27,49])