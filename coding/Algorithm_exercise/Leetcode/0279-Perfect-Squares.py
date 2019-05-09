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
        q = [(n, 0)]
        visited = {n}
        while q:
            print(q)
            num = q[-1][0]
            step = q[-1][1]
            q.pop()

            if num == 0:
                print(step)
                return step
            i = 1
            while num-i**2 >= 0:
                nextNum = num - i ** 2
                if nextNum < 0:
                    break
                if nextNum == 0:
                    return step-1
                if nextNum not in visited:
                    q.append((nextNum, step+1))
                i += 1


# Solution().numSquares(13)
Solution().numSquares(12)