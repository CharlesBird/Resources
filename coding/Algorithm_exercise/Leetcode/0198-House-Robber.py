"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(nums)
        memo = [-1] * n

        def tryRob(nums, index, memo):
            if index >= len(nums):
                return 0
            if nums[index] == -1:
                return nums[index]

            memo[index] = max(tryRob(nums, index + 1, memo), nums[index] + tryRob(nums, index + 2, memo))
            return memo[index]

        return tryRob(nums, 0, memo)


class Solution2:
    def rob(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        if not nums:
            return 0
        n = len(nums)
        memo = [-1] * n

        memo[n - 1] = nums[n - 1]
        for i in reversed(range(n - 1)):
            # i = n -2
            # while i >= 0:
            memo[i] = max(memo[i + 1], i + 2 < n and nums[i] + memo[i + 2] or nums[i])
            # i -= 1

        return memo[0]


class Solution3:
    def rob(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        pre = 0
        cur = 0
        for i in reversed(range(n)):
            tem = cur
            cur = max(cur, nums[i] + pre)
            pre = tem

        return cur


class Solution4:
    def rob(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(nums)
        memo = [-1] * n

        def tryRob(nums, index, memo):
            if index < 0:
                return 0
            if nums[index] == -1:
                return nums[index]
            res = max(tryRob(nums, index - 1, memo), nums[index] + tryRob(nums, index - 2, memo))

            memo[index] = res
            return res

        return tryRob(nums, n-1, memo)


class Solution5:
    def rob(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        if not nums:
            return 0
        n = len(nums)
        memo = [-1] * n

        memo[0] = nums[0]
        for i in range(1, n):
            memo[i] = max(memo[i - 1], i - 2 >= 0 and nums[i] + memo[i - 2] or nums[i])

        return memo[n-1]


class Solution6:
    def rob(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        pre = 0
        cur = 0
        for i in range(n):
            tem = cur
            cur = max(cur, nums[i] + pre)
            pre = tem

        return cur

nums = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
print(Solution4().rob(nums))