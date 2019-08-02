"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

"""
class Solution:
    def solveNQueens(self, n: int) -> 'List[List[str]]':

        def valid(cols, index):
            for i in range(index):
                if abs(cols[i] - cols[index]) == index - i or cols[i] == cols[index]:
                    return False
            return True

        def dfs(cols, index, path):
            if index == len(cols):
                res.append(path)
                return
            for i in range(len(cols)):
                cols[index] = i
                if valid(cols, index):
                    dfs(cols, index+1, path+["."*i+"Q"+"."*(n-i-1)])

        res = []
        dfs([-1] * n, 0, [])
        return res