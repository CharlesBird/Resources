"""Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.


A sudoku puzzle...


...and its solution numbers marked in red.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9."""
import collections
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        block = collections.defaultdict(set)
        pos = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    block[i // 3 * 3 + j // 3].add(board[i][j])
                else:
                    pos.append((i, j))

        self.dfs(board, pos, row, col, block)
        return

    def dfs(self, board, pos, row, col, block):
        if not pos:
            return True

        x, y = pos[-1]
        for n in range(1, 10):
            num = str(n)
            if num not in row[x] and num not in col[y] and num not in block[x // 3 * 3 + y // 3]:
                row[x].add(num)
                col[y].add(num)
                block[x // 3 * 3 + y // 3].add(num)
                pos.pop()
                if self.dfs(board, pos, row, col, block):
                    board[x][y] = num
                    return True
                pos.append((x, y))
                row[x].discard(num)
                col[y].discard(num)
                block[x // 3 * 3 + y // 3].discard(num)
        return False


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
sl = Solution()
sl.solveSudoku(board)
print(board)