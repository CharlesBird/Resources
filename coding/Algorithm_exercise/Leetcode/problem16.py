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
        d = {}
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                res = nums[i] + nums[l] + nums[r]
                if res > target:
                    r -= 1
                    d[res] = res - target
                elif res < target:
                    l += 1
                    d[res] = target - res

                else:
                    return target
        return min(d, key=d.get)


Solution().threeSumClosest([-1,2,1,-4], 1)
