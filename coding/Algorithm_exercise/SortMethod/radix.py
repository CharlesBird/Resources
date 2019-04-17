# 基数排序
def radixSort(myList):
    d = len(str(max(myList)))
    for i in range(d):
        bucket = [[] for _ in range(10)]
        for j in myList:
            bucket[j // (10**i) % 10].append(j)
        res = [a for b in bucket for a in b]
    return res

# radixSort([49,38,65,97,76,13,27,49])
