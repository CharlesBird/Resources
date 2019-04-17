# 桶排序，基于计数排序和特性
def bucketSort(myList):
    min_v, max_v = min(myList), max(myList)
    bucket = [0 for _ in range(max_v-min_v+1)]
    for v in myList:
        bucket[v-min_v] += 1
    res = []
    for i in range(len(bucket)):
        if bucket[i] != 0:
            res.extend([i+min_v] * bucket[i])
    return res

# bucketSort([49,-38,65,97,76,13,27,49])