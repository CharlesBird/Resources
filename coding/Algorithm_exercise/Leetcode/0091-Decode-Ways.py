"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        # Memory Search
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(s)
        memo = [-1] * n

        def dfs(s, start, memo):
            if start >= len(s):
                return 1
            if s[start] == '0':
                return 0
            if memo[start] != -1:
                return memo[start]
            res = dfs(s, start + 1, memo)
            if start + 1 < n and s[start: start + 2] <= '26':
                res += dfs(s, start + 2, memo)
            memo[start] = res
            return res

        return dfs(s, 0, memo)


class Solution2:
    def numDecodings(self, s: str) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        i = n -1
        while i >= 0:
            if s[i] != '0':
                dp[i] = dp[i + 1]
                if i + 1 < n and s[i: i + 2] <= "26":
                    dp[i] += dp[i + 2]
            i -= 1
        return dp[0]

print(Solution2().numDecodings("12"))