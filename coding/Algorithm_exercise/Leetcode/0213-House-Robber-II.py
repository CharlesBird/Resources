"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
             because they are adjacent houses.
Example 2:

Input: [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
             Total amount you can rob = 1 + 3 = 4.
"""
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        memo = [-1] * (n - 1)
        memo[0] = nums[0]
        for i in range(1, n-1):
            memo[i] = max(memo[i-1], i-2 >= 0 and nums[i] + memo[i-2] or nums[i])
        res1 = memo[n-2]
        memo[n-2] = nums[n-1]
        for i in reversed(range(1, n-1)):
            memo[i-1] = max(memo[i], i + 2 < n and nums[i] + memo[i+1] or nums[i])
        res2 = memo[0]
        return max(res1, res2)


class Solution2:
    def rob(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        if not nums:
            return 0
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        pre = 0
        cur = 0
        for i in range(n-1):
            tem = cur
            cur = max(cur, nums[i] + pre)
            pre = tem
        pre2 = 0
        cur2 = 0
        for j in reversed(range(1, n)):
            tem = cur2
            cur2 = max(cur2, nums[j] + pre2)
            pre2 = tem
        return max(cur, cur2)

nums = [2,3,2]
# nums = [1,2,1,1]
Solution2().rob(nums)