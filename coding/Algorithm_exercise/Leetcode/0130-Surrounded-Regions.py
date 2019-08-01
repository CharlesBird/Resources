"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:

Surrounded regions shouldn’t be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.

"""
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(board, x, y):
            q = [(x, y)]
            visited[x][y] = True
            ret = True
            while q:
                curX, curY = q[0]
                del q[0]
                record.append((curX, curY))
                for i in range(len(d)):
                    newX = curX + d[i][0]
                    newY = curY + d[i][1]
                    if newX < 0 or newX >= len(board) or newY < 0 or newY >= len(board[0]):
                        ret = False
                    elif board[newX][newY] == 'O' and not visited[newX][newY]:
                        q.append((newX, newY))
                        visited[newX][newY] = True

            return ret

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'O' and not visited[x][y]:
                    record = []
                    if bfs(board, x, y):
                        for r in record:
                            board[r[0]][r[1]] = 'X'


class Solution2:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(board, x, y):
            stack = [(x, y)]
            visited[x][y] = True
            ret = True
            while stack:
                curX, curY = stack.pop()
                record.append((curX, curY))
                for i in range(len(d)):
                    newX = curX + d[i][0]
                    newY = curY + d[i][1]
                    if newX < 0 or newX >= len(board) or newY < 0 or newY >= len(board[0]):
                        ret = False
                    elif board[newX][newY] == 'O' and not visited[newX][newY]:
                        stack.append((newX, newY))
                        visited[newX][newY] = True

            return ret

        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == 'O' and not visited[x][y]:
                    record = []
                    if dfs(board, x, y):
                        for r in record:
                            board[r[0]][r[1]] = 'X'


Solution().solve([["O","X","O"],["X","O","X"],["O","X","O"]])