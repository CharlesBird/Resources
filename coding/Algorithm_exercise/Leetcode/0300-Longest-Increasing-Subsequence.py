"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
"""
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 记忆化搜索
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        n = len(nums)
        if not n:
            return 0
        memo = [0] * n

        def helper(nums, index):
            if memo[index] != 0:
                return memo[index]

            res = 1
            for i in range(index):
                if nums[index] > nums[i]:
                    res = max(res, helper(nums, i) + 1)

            memo[index] = res

            return res

        res = 1
        for i in range(n):
            res = max(res, helper(nums, i))

        return res


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 动态规划
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        n = len(nums)
        if not n:
            return 0
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            res = 1
            for j in range(i):
                if nums[i] > nums[j]:
                    res = max(res, dp[j] + 1)

            dp[i] = res

        return max(dp)


class Solution3:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 动态规划+二分查找法
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        import bisect
        dp = []
        for num in nums:
            if not dp or dp[-1] < num:
                dp.append(num)
            else:
                index = bisect.bisect_left(dp, num)
                dp[index] = num
        return len(dp)


# nums = [10,9,2,5,3,7,101,18]
nums = [10,9,2,5,3,7,101,18, 1, 6, 8, 11, 12]
res = Solution3().lengthOfLIS(nums)
print(res)