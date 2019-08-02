"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3
"""
class Solution:
    def numIslands(self, grid: "List[List[str]]") -> int:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(grid, visited, i, j):
            visited[i][j] = True
            for k in range(len(d)):
                newi = i + d[k][0]
                newj = j + d[k][1]
                if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]) and not visited[newi][newj] and grid[newi][newj] == '1':
                    dfs(grid, visited, newi, newj)

        if not grid:
            return 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(grid, visited, i, j)
                    res += 1
        return res


class Solution2:
    def numIslands(self, grid: "List[List[str]]") -> int:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(grid, visited, i, j):
            q = [(i, j)]
            visited[i][j] = True
            while q:
                curi, curj = q[0]
                del q[0]
                for k in range(len(d)):
                    newi = curi + d[k][0]
                    newj = curj + d[k][1]
                    if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]) and not visited[newi][newj] and grid[newi][newj] == '1':
                        q.append((newi, newj))
                        visited[newi][newj] = True

        if not grid:
            return 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    bfs(grid, visited, i, j)
                    res += 1
        return res


class Solution3:
    def numIslands(self, grid: "List[List[str]]") -> int:
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(grid, visited, i, j):
            stack = [(i, j)]
            visited[i][j] = True
            while stack:
                curi, curj = stack.pop()
                for dx, dy in d:
                    newi = curi + dx
                    newj = curj + dy
                    if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]) and not visited[newi][newj] and grid[newi][newj] == '1':
                        stack.append((newi, newj))
                        visited[newi][newj] = True

        if not grid:
            return 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(grid, visited, i, j)
                    res += 1
        return res


Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])