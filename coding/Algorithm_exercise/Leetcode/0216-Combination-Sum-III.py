"""


Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

    All numbers will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
"""
class Solution:
    def combinationSum3(self, k: int, n: int) -> "List[List[int]]":

        def dfs(nums, index, k, target, path, res):
            if k == 0 and target == 0:
                res.append(path)
                return
            for i in range(index, len(nums)):
                dfs(nums, i+1, k-1, target-nums[i], path+[nums[i]], res)

        res = []
        dfs([i for i in range(1, 10)], 0, k, n, [], res)
        return res


class Solution2:
    """[1-99] 中选出10个数 和为100"""
    def combinationSum3(self, k: int, n: int) -> "List[List[int]]":

        def dfs(index, k, target, path, res):
            if k == 0 and target == 0:
                res.append(path)
                return
            if k < 0 or target < 0:
                return
            for i in range(index, 100):
                dfs(i+1, k-1, target-i, path+[i], res)

        res = []
        dfs(1, k, n, [], res)
        return res

Solution2().combinationSum3(10, 100)
