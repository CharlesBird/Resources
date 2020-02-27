"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.


Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].


Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
"""
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Time Complexity: O(n)*0(len(sums))
        # Space Complexity: O(len(sums))
        sums = sum(nums)

        if sums % 2:
            return False
        target = sums // 2

        memo = set([0])

        for i in nums:
            memo.update([i + j for j in memo])
            if target in memo:
                return True

        return False


class Solution2:
    def canPartition(self, nums: List[int]) -> bool:
        # Time Complexity: O(len(nums) * O(sum(nums)))
        # Space Complexity: O(len(nums) * O(sum(nums)))
        sums = sum(nums)
        n = len(nums)

        if sums % 2:
            return False

        memo = [[-1] * (sums // 2 + 1) for _ in range(n)]

        def helper(nums, index, sums, memo):
            if sums == 0:
                return True
            if sums < 0 or index < 0:
                return False
            if memo[index][sums] != -1:
                return memo[index][sums] == 1

            memo[index][sums] = helper(nums, index - 1, sums, memo) or (
                        helper(nums, index - 1, sums - nums[index], memo) and 1 or 0)

            return memo[index][sums] == 1

        return helper(nums, n - 1, sums // 2, memo)


class Solution3:
    def canPartition(self, nums: List[int]) -> bool:
        # Time Complexity: O(len(nums) * O(sum(nums)))
        # Space Complexity: O(len(nums) * O(sum(nums)))
        sums = sum(nums)
        n = len(nums)

        if sums % 2:
            return False

        target = sums // 2

        memo = [False] * (target + 1)

        for i in range(target + 1):
            memo[i] = nums[0] == i

        for i in range(1, n):
            j = target
            while j >= nums[i]:
                memo[j] = memo[j] or memo[j - nums[i]]
                j -= 1

        return memo[target]


Solution3().canPartition([1,5,11,5])