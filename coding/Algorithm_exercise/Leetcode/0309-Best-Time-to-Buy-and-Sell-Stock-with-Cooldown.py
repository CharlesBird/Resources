"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
"""
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(prices)
        if n <= 1:
            return 0

        sell = [-1] * n
        buy = [-1] * n

        def _sell(prices, index, buy, sell):
            if index == 0:
                return 0
            if index == 1:
                return max(0, prices[1] - prices[0])
            if sell[index] != -1:
                return sell[index]

            res = max(_sell(prices, index - 1, buy, sell), _buy(prices, index - 1, buy, sell) + prices[index])
            sell[index] = res
            return res

        def _buy(prices, index, buy, sell):
            if index == 0:
                return -prices[0]
            if index == 1:
                return max(-prices[0], -prices[1])
            if buy[index] != -1:
                return buy[index]

            res = max(_buy(prices, index - 1, buy, sell), _sell(prices, index - 2, buy, sell) - prices[index])
            buy[index] = res
            return res

        return _sell(prices, n - 1, buy, sell)


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(prices)
        if n <= 1:
            return 0

        sell = [0] * n
        buy = [0] * n

        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        sell[1] = max(0, buy[0] + prices[1])

        for i in range(2, n):
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])

        print(buy, sell)

        return sell[n - 1]


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(prices)
        if n <= 1:
            return 0

        buy = [-prices[0], max(-prices[0], -prices[1]), 0]
        sell = [0, max(0, prices[1] - prices[0]), 0]

        for i in range(2, n):
            sell[i % 3] = max(sell[(i - 1) % 3], buy[(i - 1) % 3] + prices[i])
            buy[i % 3] = max(buy[(i - 1) % 3], sell[(i - 2) % 3] - prices[i])

        return sell[(n - 1) % 3]


prices = [1,2,3,0,2]
Solution2().maxProfit(prices)