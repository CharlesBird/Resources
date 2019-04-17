import random
import time
import numpy as np
from bucket import bucketSort
from bubble import bubbleSort
from counting import countingSort
from heap import heapSort
from insertion import insertionSort
from merge import mergeSort
from quick import quickSort
from radix import radixSort
from selection import selectionSort
from shell import shellSort

def main(method, ran, size):
    arg = [random.randint(1, ran) for _ in range(size)]
    start = time.time()
    eval("{}({})".format(method, arg))
    t = time.time() - start
    return t


if __name__ == '__main__':
    for i in [100, 1000, 10000, 100000]:
        for j in [100, 1000, 10000]:
            print('range{}_{}'.format(i, j))
            for name in ['bubbleSort', 'selectionSort', 'insertionSort', 'shellSort', 'mergeSort', 'quickSort', 'heapSort', 'countingSort', 'bucketSort', 'radixSort']:
                res = [main(name, i, j), main(name, i, j), main(name, i, j)]
                print('排序方式{}, 数字范围{}, 排序长度{}, 三次耗时: {}, 平均耗时: {}'.format(name, i, j, res, np.mean(res)))