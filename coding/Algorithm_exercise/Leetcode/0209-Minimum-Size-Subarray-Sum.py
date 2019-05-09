"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example:

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
"""
class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        sums = 0
        i = 0
        res = len(nums) + 1
        for j, v in enumerate(nums):
            sums += v
            while sums >= s:
                res = min(res, j-i+1)
                sums -= nums[i]
                i += 1
        return res <= len(nums) and res or 0



# res=Solution().minSubArrayLen(7, [2,3,1,2,4,3])
# res=Solution().minSubArrayLen(15, [1,2,3,4,5])
res=Solution().minSubArrayLen(213,[12,28,83,4,25,26,25,2,25,25,25,12])


print(res)