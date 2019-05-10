"""
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
class Solution:
    def numSquares(self, n: int) -> int:

        # dp = [0]
        # while len(dp) <= n:
        #     MIN = min(dp[-j * j] for j in range(1, int(len(dp) ** 0.5 + 1)))
        #     dp.append(MIN + 1)
        # return dp[n]

        # Method Two
        q = [(n, 0)]
        visited = [False] * (n+1)
        while q:
            num = q[0][0]
            step = q[0][1]
            q.pop(0)

            i = 1
            while num-i**2 >= 0:
                nextNum = num - i ** 2
                if nextNum < 0:
                    break
                if nextNum == 0:
                    return step+1
                if not visited[nextNum]:
                    q.append((nextNum, step+1))
                    visited[nextNum] = True
                i += 1


# Solution().numSquares(13)
Solution().numSquares(12)