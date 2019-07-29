"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution:
    def combine(self, n: int, k: int) -> "List[List[int]]":

        def dfs(nums, k, path, res):
            if len(path) == k:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[i+1:], k, path+[nums[i]], res)

        res = []
        dfs([i for i in range(1, n+1)], k, [], res)
        return res


class Solution2:
    def combine(self, n: int, k: int) -> "List[List[int]]":
        from itertools import combinations

        return list(combinations(range(1, n+1), k))


Solution2().combine(4, 2)