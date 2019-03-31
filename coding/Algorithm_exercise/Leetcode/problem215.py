# 215. Kth Largest Element in an Array
"""
Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

"""
from heapq import nlargest
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # nlargest(k, nums)
        # 快速排序法
        # while k < len(nums):
        #     mid = nums[0]
        return  sorted(nums, reverse=True)[k - 1]


Solution().findKthLargest([3,2,1,5,6,4],3)