"""
In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:

The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.


Example 1:

Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are “10,”0001”,”1”,”0”


Example 2:

Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
"""
from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 递归
        # Time Complexity: O(len(strs)*m*n)
        # Space Complexity: O(len(strs)*m*n)
        len_s = len(strs)
        mcost = [0] * len_s
        ncost = [0] * len_s
        for i, s in enumerate(strs):
            for c in s:
                if c == '0':
                    mcost[i] += 1
                else:
                    ncost[i] += 1

        memo = [[[-1] * (n + 1) for _ in range(m + 1)] for _ in range(len_s)]

        def helper(index, m, n, memo, mcost, ncost):
            if index < 0:
                return 0
            if memo[index][m][n] != -1:
                return memo[index][m][n]

            memo[index][m][n] = helper(index - 1, m, n, memo, mcost, ncost)

            if m >= mcost[index] and n >= ncost[index]:
                memo[index][m][n] = max(memo[index][m][n],
                                        1 + helper(index - 1, m - mcost[index], n - ncost[index], memo, mcost, ncost))

            return memo[index][m][n]

        return helper(len_s - 1, m, n, memo, mcost, ncost)


class Solution2:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # 动态规划
        # Time Complexity: O(len(strs)*m*n)
        # Space Complexity: O(len(strs)*m*n)
        len_s = len(strs)
        mcost = [0] * len_s
        ncost = [0] * len_s
        for i, s in enumerate(strs):
            for c in s:
                if c == '0':
                    mcost[i] += 1
                else:
                    ncost[i] += 1

        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len_s)]

        for i in range(mcost[0], m + 1):
            for j in range(ncost[0], n + 1):
                dp[0][i][j] = 1

        for k in range(1, len_s):
            for x in range(m + 1):
                for y in range(n + 1):
                    dp[k][x][y] = dp[k - 1][x][y]
                    if x >= mcost[k] and y >= ncost[k]:
                        dp[k][x][y] = max(dp[k][x][y], 1 + dp[k - 1][x - mcost[k]][y - ncost[k]])

        return dp[len_s - 1][m][n]


class Solution3:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Time Complexity: O(len(strs)*m*n)
        # Space Complexity: O(m*n)
        len_s = len(strs)
        mcost = [0] * len_s
        ncost = [0] * len_s
        for i, s in enumerate(strs):
            for c in s:
                if c == '0':
                    mcost[i] += 1
                else:
                    ncost[i] += 1

        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(2)]

        for i in range(mcost[0], m + 1):
            for j in range(ncost[0], n + 1):
                dp[0][i][j] = 1

        for k in range(1, len_s):
            for x in range(m + 1):
                for y in range(n + 1):
                    dp[k % 2][x][y] = dp[(k - 1) % 2][x][y]
                    if x >= mcost[k] and y >= ncost[k]:
                        dp[k % 2][x][y] = max(dp[k % 2][x][y], 1 + dp[(k - 1) % 2][x - mcost[k]][y - ncost[k]])

        return dp[(len_s - 1) % 2][m][n]


class Solution4:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Time Complexity: O(len(strs)*m*n)
        # Space Complexity: O(m*n)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i, s in enumerate(strs):
            mcost, ncost = 0, 0
            for c in s:
                if c == '0':
                    mcost += 1
                else:
                    ncost += 1

            for x in reversed(range(mcost, m + 1)):
                for y in reversed(range(ncost, n + 1)):
                    dp[x][y] = max(dp[x][y], 1 + dp[x - mcost][y - ncost])

        return dp[m][n]


class Solution5:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Time Complexity: O(len(strs)*m*n)
        # Space Complexity: O(m*n)
        # 耗时最短
        import numpy as np
        dp = np.zeros([m + 1, n + 1])
        for i, s in enumerate(strs):
            zeros, ones = s.count('0'), s.count('1')

            if m >= zeros and n >= ones:
                dp[zeros:m + 1, ones:n + 1] = np.maximum(dp[zeros:m + 1, ones:n + 1],
                                                         dp[0:m + 1 - zeros, 0:n + 1 - ones] + 1)

        return int(dp[m][n])


strs = ["10","0001","111001","1","0"]
m, n = 5, 3
res = Solution5().findMaxForm(strs, m, n)
print(res)