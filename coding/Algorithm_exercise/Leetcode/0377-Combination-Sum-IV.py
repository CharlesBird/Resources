"""
Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.


Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?
"""
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(n * target)
        # Space Complexity: O(target)
        memo = [-1] * (target + 1)

        def helper(nums, target, memo):
            if target == 0:
                return 1
            if memo[target] != -1:
                return memo[target]

            res = 0
            for i in nums:
                if target - i >= 0:
                    res += helper(nums, target - i, memo)

            memo[target] = res
            return res

        return helper(nums, target, memo)


class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Time Complexity: O(n * target)
        # Space Complexity: O(target)
        dp = [0] * (target + 1)

        dp[0] = 1

        for i in range(1, target + 1):
            for j in nums:
                if i - j >= 0:
                    dp[i] += dp[i - j]

        return dp[target]


nums = [1, 2, 3]
target = 4
Solution2().combinationSum4(nums, target)