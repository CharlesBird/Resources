# 16. 3Sum Closest
"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""
class Solution:
    def threeSumClosest(self, nums: 'List[int]', target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        for i in range(l, len(nums)):
            if l == i:
                continue
            while l < r:
                res = nums[l] + nums[i] + nums[r]
                closest = res - target
                if closest == 0:
                    return