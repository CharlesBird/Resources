
"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
"""
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 三路快排方法
        l = -1
        r = len(nums)
        i = 0
        while i < r:
            if nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                r -= 1
                nums[i], nums[r] = nums[r], nums[i]
            else:
                l += 1
                nums[l], nums[i] = nums[i], nums[l]
                i += 1
        return nums

Solution().sortColors([2,0,2,1,1,0])

