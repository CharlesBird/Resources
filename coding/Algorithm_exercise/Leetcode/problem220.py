# 220. Contains Duplicate III
"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3, t = 0
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1, t = 2
Output: true
Example 3:

Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
"""
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: 'List[int]', k: int, t: int) -> bool:
        # 为什么需要判断t=0的情况，否则会出现超时
        s = set()
        for i in range(len(nums)):
            if t == 0:
                if nums[i] in s:
                    return True
            else:
                for ele in s:
                    if abs(nums[i] - ele) <= t:
                        return True
            s.add(nums[i])
            if len(s) == k + 1:
                s.remove(nums[i - k])
        return False

Solution().containsNearbyAlmostDuplicate([3,6,0,2],2,2)