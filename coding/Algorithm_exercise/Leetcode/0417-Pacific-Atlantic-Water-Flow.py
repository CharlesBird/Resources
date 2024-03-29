"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

    The order of returned grid coordinates does not matter.
    Both m and n are less than 150.



Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""
from typing import List

class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(visited, x, y):
            visited[x][y] = True
            for dx, dy in d:
                newX = x + dx
                newY = y + dy
                if 0 <= newX < m and 0 <= newY < n and not visited[newX][newY] and matrix[newX][newY] >= matrix[x][y]:
                    dfs(visited, newX, newY)

        res = []
        if not matrix:
            return res
        m, n = len(matrix), len(matrix[0])
        pacific = [[False for _ in range(n)] for _ in range(m)]
        atlantic = [[False for _ in range(n)] for _ in range(m)]

        for i in range(m):
            dfs(pacific, i, 0)
            dfs(atlantic, i, n-1)

        for j in range(n):
            dfs(pacific, 0, j)
            dfs(atlantic, m-1, j)

        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res


Solution().pacificAtlantic([[1,1],[1,1],[1,1]])

