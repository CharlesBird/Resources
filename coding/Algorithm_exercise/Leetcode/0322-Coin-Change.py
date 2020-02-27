"""
You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time Complexity: O(len(coins) * amount)
        # Space Complexity: O(amount)
        memo = [-1] * (amount + 1)

        def helper(coins, amount, memo):
            if amount == 0:
                return 0
            if memo[amount] != -1:
                return memo[amount]

            res = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + helper(coins, amount - coin, memo))
            memo[amount] = res
            return res

        res = helper(coins, amount, memo)
        return res == float('inf') and -1 or res


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time Complexity: O(len(coins) * amount)
        # Space Complexity: O(amount)
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] == float('inf') and -1 or dp[amount]


class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Time Complexity: O(len(coins) * amount)
        # Space Complexity: O(amount)
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] == float('inf') and -1 or dp[amount]


coins = [1,2,5]
amount = 11
Solution2().coinChange(coins, amount)