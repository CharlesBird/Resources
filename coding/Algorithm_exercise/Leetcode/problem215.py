# 215. Kth Largest Element in an Array
from heapq import nlargest
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # nlargest(k, nums)
        # 快速排序法
        # while k < len(nums):
        #     mid = nums[0]
        return  sorted(nums, reverse=True)[k - 1]


Solution().findKthLargest([3,2,1,5,6,4],3)