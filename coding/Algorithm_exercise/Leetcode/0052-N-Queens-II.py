"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
class Solution:
    def totalNQueens(self, n: int) -> int:

        def valid(cols, index):
            for i in range(index):
                if abs(cols[i] - cols[index]) == index - i or cols[i] == cols[index]:
                    return False
            return True

        def dfs(cols, index):
            res = 0
            if index == len(cols):
                return 1
            for i in range(len(cols)):
                cols[index] = i
                if valid(cols, index):
                    res += dfs(cols, index+1)
            return res

        res = dfs([-1] * n, 0)
        return res