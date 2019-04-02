# 11. Container With Most Water
"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

"""
class Solution:
    def maxArea(self, height) -> int:
        i = 0
        j = len(height) - 1
        res = 0
        while i < j:
            res = max(min(height[i], height[j]) * (j - i), res)
            if height[i] < height[j]:
                i += 1
            else:
                j-=1
        return res
res=Solution().maxArea([2,3,10,5,7,8,9])
print(res)