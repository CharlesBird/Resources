"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
class Solution:
    def exist(self, board: 'List[List[str]]', word: str) -> bool:

        def dfs(board, word, visited, i, j):
            if not word:
                return True
            if i < 0 or i == len(board) or j < 0 or j == len(board[0]) or visited[i][j] or word[0] != board[i][j]:
                return False
            visited[i][j] = True
            res = dfs(board, word[1:], visited, i+1, j) or dfs(board, word[1:], visited, i-1, j) or \
                  dfs(board, word[1:], visited, i, j+1) or dfs(board, word[1:], visited, i, j-1)
            visited[i][j] = False
            return res

        if not board:
            return False
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, visited, i, j):
                    return True
        return False
