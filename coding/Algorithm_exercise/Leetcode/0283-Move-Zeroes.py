"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:

    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
"""
class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # method one
        # k = 0
        # for num in nums:
        #     if num:
        #         nums[k] = num
        #         k += 1
        # for i in range(k, len(nums)):
        #     nums[i] = 0
        # print(nums)
        # method two
        k = 0
        for i, num in enumerate(nums):
            if num:
                if k != i:
                    nums[k], nums[i] = nums[i], nums[k]
                    k += 1
                else:
                    k += 1
        print(nums)


# Solution().moveZeroes([0,1,0,3,12])
Solution().moveZeroes([0,1,0])
