
"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o
+------------->
0  1  2  3  4

Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
"""
import collections
# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points: 'List[Point]') -> int:

        ans = 0
        upoints = collections.defaultdict(int)

        for p in points:
            upoints[(p.x, p.y)] += 1

        while upoints:
            (pxi, pyi), uxi = upoints.popitem()
            linesi = collections.defaultdict(lambda: uxi)
            if upoints:
                for (pxj, pyj), uxj in upoints.items():
                    h = (pyj - pyi) / (pxj - pxi) if pxj != pxi else 0
                    linesi[h] += uxj
                ans = max(ans, max(linesi.values()))
            else:
                ans = max(ans, uxi)

        return ans
        # if len(points) == 1:
        #     return 1
        # from collections import defaultdict
        # d = defaultdict(dict)
        # for i, p_obj in enumerate(points):
        #     x = p_obj.x
        #     y = p_obj.y
        #     eq_p = 0
        #     for j, p_obj2 in enumerate(points):
        #         if i != j:
        #             if not (y-p_obj2.y) and not (x-p_obj2.x):
        #                 d[i]['=y'] = d[i].get('=y', 1) + 1
        #                 d[i]['=x'] = d[i].get('=x', 1) + 1
        #                 eq_p += 1
        #             elif not (y-p_obj2.y) and (x-p_obj2.x):
        #                 d[i]['=y'] = d[i].get('=y', 1) + 1
        #             elif (y-p_obj2.y) and not (x-p_obj2.x):
        #                 d[i]['=x'] = d[i].get('=x', 1) + 1
        #             else:
        #                 grad = '%.16f' % ((x - p_obj2.x) / (y - p_obj2.y))
        #                 d[i][grad] = d[i].get(grad, 1) + 1
        #     for grad in d[i]:
        #         if grad not in ('=y', '=x'):
        #             d[i][grad] += eq_p
        # grad_count = d.values()
        # res = set()
        # for l in grad_count:
        #     res = res.union(set(l.values()))
        # return len(res) and max(res) or 0

# Solution().maxPoints([Point(1,1), Point(2,2), Point(3,3)])
# Solution().maxPoints([Point(1,1), Point(3,2), Point(5,3),Point(4,1),Point(2,3),Point(1,4)])
# Solution().maxPoints([Point(0,0), Point(0,0)])
# Solution().maxPoints([Point(1,1), Point(1,1), Point(2,2), Point(2,2)])
Solution().maxPoints([Point(0,0), Point(94911151,94911150), Point(94911152,94911151)])
