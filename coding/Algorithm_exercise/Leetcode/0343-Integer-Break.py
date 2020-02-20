"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
Note: You may assume that n is not less than 2 and not larger than 58.
"""
class Solution:
    def integerBreak(self, n: int) -> int:
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        dp = [1] * (n+1)
        for i in range(3, n+1):
            for j in range(2, i):
                print('dp = ', dp)
                print('i={}, j={}, dp[i]={}, j * (i - j)={}, i - j={}, dp[i - j] * j={}'.format(i, j, dp[i], j * (i - j), i - j, dp[i - j] * j))
                print('========================')
                dp[i] = max(dp[i], max(j * (i - j), dp[i - j] * j))
        return dp[n]


class Solution2:
    def integerBreak(self, n: int) -> int:
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        if n == 2:
            return 1
        if n == 3:
            return 2
        memo = [1] * (n+1)
        memo[0] = 0
        memo[1] = 1
        memo[2] = 2
        memo[3] = 3
        for i in range(2, n+1):
            for j in (1, (i+1)//2):
                memo[i] = max(memo[i], memo[j] * memo[i - j])

        print(memo)
        return memo[n]


s = Solution2()
print(s.integerBreak(8))