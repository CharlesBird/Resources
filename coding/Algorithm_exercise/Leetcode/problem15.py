# 15. 3Sum
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution:
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':
        from collections import Counter
        res = []
        n_count = Counter(nums)
        left, right = [], []
        for v in n_count:
            if v > 0:
                right.append(v)
            elif v < 0:
                left.append(v)
        if 0 in n_count and n_count[0] > 2:
            res.append([0,0,0])
        left.sort()
        right.sort()
        for i in left:
            for j in right:
                k = 0 - i - j
                if k in n_count:
                    if k in (i, j):
                        if n_count[k] > 1:
                            res.append([i, k, j])
                    elif i < k < j:
                        res.append([i, k, j])
        # nums.sort()
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     l = i + 1
        #     r = len(nums) - 1
        #     while l < r:
        #         target = nums[l] + nums[i] + nums[r]
        #         if target > 0:
        #             r -= 1
        #         elif target < 0:
        #             l += 1
        #         else:
        #             res.append([nums[i], nums[l], nums[r]])
        #             while l < r and nums[l] == nums[l+1]:
        #                 l += 1
        #             while l < r and nums[r] == nums[r - 1]:
        #                 r -= 1
        #             l += 1
        #             r -= 1
        return res

Solution().threeSum([0,0,0])