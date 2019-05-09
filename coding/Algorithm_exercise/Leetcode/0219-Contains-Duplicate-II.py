"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""
class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: int) -> bool:
        # Method Three
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
            if len(s) == k + 1:
                s.remove(nums[i-k])
        return False
        # Method One
        # if len(nums) == len(set(nums)):
        #     return False
        # for i in range(len(nums)-1):
        #     for j in range(i+1, min(i+k+1, len(nums))):
        #         if nums[i] == nums[j]:
        #             return True
        # return False

        # Method Two
        # d = {}
        # for i, v in enumerate(nums):
        #     if v in d and i - d[v] <= k:
        #         return True
        #     d[v] = i
        #
        # return False

Solution().containsNearbyDuplicate([1,0,1,1],1)