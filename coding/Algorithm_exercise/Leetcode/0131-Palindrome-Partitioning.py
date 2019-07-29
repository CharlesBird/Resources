"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""

class Solution:
    def partition(self, s: str) -> "List[List[str]]":
        def dfs(s, curr, res):
            if not s:
                res.append(curr)
                return
            for i in range(1, len(s)+1):
                if self.isPal(s[:i]):
                    dfs(s[i:], curr+[s[:i]], res)

        res = []
        dfs(s, [], res)
        return res

    def isPal(self, s):
        return s == s[::-1]
