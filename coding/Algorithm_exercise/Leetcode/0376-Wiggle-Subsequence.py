"""
A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?
"""
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 递归，超时
        # Time Complexity: O(n!)
        # Space Complexity: O(n)
        if len(nums) < 2:
            return len(nums)

        def helper(nums, index, isUp):
            res = 0
            for i in range(index + 1, len(nums)):
                if (isUp and nums[i] > nums[index]) or (not isUp and nums[i] < nums[index]):
                    res = max(res, 1 + helper(nums, i, not isUp))

            return res

        return 1 + max(helper(nums, 0, True), helper(nums, 0, False))


class Solution2:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 动态规划
        # Time Complexity: O(n^2)
        # Space Complexity: O(n)
        import collections
        n = len(nums)
        if n < 2:
            return n

        up = collections.defaultdict(int)
        down = collections.defaultdict(int)

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    up.update({i: max(up[i], down[j] + 1)})
                elif nums[i] < nums[j]:
                    down.update({i: max(down[i], up[j] + 1)})

        return 1 + max(down[n - 1], up[n - 1])


class Solution3:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 动态规划
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        n = len(nums)
        if n < 2:
            return n

        up = [0] * n
        down = [0] * n

        up[0] = 1
        down[0] = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                down[i] = down[i - 1]
                up[i] = up[i - 1]

        return max(down[n - 1], up[n - 1])


class Solution4:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 动态规划, 无新增空间
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        if n < 2:
            return n

        up = down = 1

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1

        return max(down, up)


class Solution5:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(nums)
        if n < 2:
            return n

        prediff = nums[1] - nums[0]
        res = prediff != 0 and 2 or 1
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prediff <= 0) or (diff < 0 and prediff >= 0):
                res += 1
                prediff = diff

        return res


nums = [33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15]
res = Solution().wiggleMaxLength(nums)
print(res)