"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)


class Solution2:
    def climbStairs(self, n: int) -> int:
        memo = [1, 2]
        for i in range(2, n):
            memo.append(memo[i - 1] + memo[i - 2])
        return memo[n - 1]


class Solution3:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        first = 1
        second = 2
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
        return second


class Solution4:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        base = [(1, 1), (1, 0)]
        return self.matrix_pow(base, n)[0][0]

    def matrix_pow(self, m, n):
        if n == 1:
            return m
        t = self.matrix_pow(m, n // 2)
        res = self.matrix_multiply(t, t);
        if n % 2:
            return self.matrix_multiply(res, m);
        return res;

    def matrix_multiply(self, a, b):
        c = [[None, None], [None, None]]
        for i in range(2):
            for j in range(2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]
        return c


import math
class Solution5:
    def climbStairs(self, n: int) -> int:
        sqrt5 = math.sqrt(5)
        return int((math.pow((1+sqrt5) / 2, n+1) - math.pow((1-sqrt5) / 2, n+1)) / sqrt5)


s = Solution2()
print(s.climbStairs(10))