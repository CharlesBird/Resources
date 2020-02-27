"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # 递归，超时
        # Time Complexity: O(2^n)
        # Space Complexity: O(n)

        def helper(index, res):
            if index == len(nums):
                return res == S and 1 or 0

            ret = 0
            ret += helper(index + 1, res + nums[index])
            ret += helper(index + 1, res - nums[index])
            return ret

        return helper(0, 0)


class Solution2:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # 记忆化搜索
        # Time Complexity: O(n * maxNum * log(n * maxNum))
        # Space Complexity: O(n * maxNum)
        memo = {}

        def helper(index, S):
            if index == len(nums):
                return S == 0 and 1 or 0

            p = (index, S)
            if p in memo:
                return memo[p]

            ret = 0
            ret += helper(index + 1, S + nums[index])
            ret += helper(index + 1, S - nums[index])
            memo.update({p: ret})
            return ret

        return helper(0, S)


class Solution3:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # 栈方式，运行效率超时
        # Time Complexity: O(2^n)
        # Space Complexity: O(2^n)
        indexStack, sumStack = [0], [0]

        res = 0

        while indexStack:
            index = indexStack.pop()
            sums = sumStack.pop()

            if index + 1 == len(nums):
                res += (sums + nums[index] == S) + (sums - nums[index] == S)
            else:
                indexStack.append(index + 1)
                sumStack.append(sums + nums[index])
                indexStack.append(index + 1)
                sumStack.append(sums - nums[index])

        return res


class Solution4:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # 动态规划
        # Time Complexity: O(n*len(S))
        # Space Complexity: O(n)
        import collections
        dp = collections.defaultdict(int)

        dp[nums[0]] += 1
        dp[-nums[0]] += 1

        for num in nums[1:]:
            tem = collections.defaultdict(int)
            for k, v in dp.items():
                tem[k + num] += dp[k]
                tem[k - num] += dp[k]
            dp = tem

        return dp[S]


# nums = [42,36,4,15,17,15,31,1,11,2,12,28,22,9,2,31,48,18,48,5]
# s = 15
nums = [50,37,6,20,35,41,45,3,20,36,49,1,20,10,43,4,44,15,44,34]
s = 25
# nums = [1,1,1,1,1]
# s = 3
res = Solution4().findTargetSumWays(nums, s)
print(res)