"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(n*m)
        # Space Complexity: O(n*m)
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

        return dp[m - 1][n - 1]


class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(n*m)
        # Space Complexity: O(2*n)
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = grid[0][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        for i in range(1, m):
            dp[i % 2][0] = dp[(i - 1) % 2][0] + grid[i][0]
            for j in range(1, n):
                dp[i % 2][j] = min(dp[(i - 1) % 2][j], dp[i % 2][j - 1]) + grid[i][j]

        return dp[(m - 1) % 2][n - 1]


class Solution3:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(n*m)
        # Space Complexity: O(n)
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n
        dp[0] = grid[0][0]
        for j in range(1, n):
            dp[j] = dp[j - 1] + grid[0][j]

        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[n - 1]

s = Solution2()
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(s.minPathSum(grid))