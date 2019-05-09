"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution:
    def twoSum(self, nums: 'List[int]', target: int) -> 'List[int]':
        d = {}
        for i, v in enumerate(nums):
            v2 = target - v
            if v2 in d:
                return [d[v2], i]
            else:
                d[v] = i
        #     if v2 in nums:
        #         j = nums.index(v2)
        #         if i == j:
        #             continue
        #         else:
        #             return [i, j]
        # return []