# 447. Number of Boomerangs
"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:

Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""
class Solution:
    def numberOfBoomerangs(self, points: 'List[List[int]]') -> int:
        res =0
        i = 0
        while i < len(points):
            dict_count = {}
            for j, p in enumerate(points):
                if i != j:
                    dis = (p[0] - points[i][0]) * (p[0] - points[i][0]) + (p[1] - points[i][1]) * (p[1] - points[i][1])
                    dict_count[dis] = dict_count.get(dis, 0) + 1
            for c in dict_count.values():
                if c > 1:
                    res += c * (c - 1)
            i += 1
        return res

Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]])