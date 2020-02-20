"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""
from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 自顶向下，记忆化搜索
        n = len(triangle)
        memo = [0] * n
        memo[0] = triangle[0][0]
        for i in range(1, n):
            for j in reversed(range(i+1)):
                if j == i:
                    memo[j] = triangle[i][j] + memo[j-1]
                elif j > 0:
                    memo[j] = triangle[i][j] + min(memo[j-1], memo[j])
                elif j == 0:
                    memo[j] = triangle[i][j] + memo[j]
        return min(memo)


class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 自底向上，动态规划
        n = len(triangle)
        memo = triangle[-1]
        for i in reversed(range(n-1)):
            for j in range(i+1):
                memo[j] = triangle[i][j] + min(memo[j], memo[j+1])
        return memo[0]


class Solution3:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 记忆化搜索，缓存方式
        from functools import lru_cache
        @lru_cache(None)
        def helper(row, col):
            if row == len(triangle) - 1:
                return triangle[row][col]
            else:
                return triangle[row][col] + min(helper(row + 1, col), helper(row + 1, col + 1))

        return helper(0, 0)