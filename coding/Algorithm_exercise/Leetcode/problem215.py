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
class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        # 快速排序法
        def quickSort(nums, start, end):
            if start < end:
                i, j = start, end
                pivot = nums[i]
                while i < j:
                    while i < j and nums[j] >= pivot:
                        j -= 1
                    nums[i] = nums[j]
                    while i < j and nums[i] <= pivot:
                        i += 1
                    nums[j] = nums[i]
                nums[i] = pivot
                quickSort(nums, start, i-1)
                quickSort(nums, j+1, end)

            return nums
        quickSort(nums, 0, len(nums)-1)
        print(nums[-k])



        # return sorted(nums, reverse=True)[k - 1]


Solution().findKthLargest([3,2,1,5,6,4],3)