"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]

Note:

    The order of output does not matter.
    The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
    The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
"""
class Solution:
    def readBinaryWatch(self, num: int) -> "List[str]":

        def dfs(n, hours, mins, index, res):
            if hours >= 12 or mins >= 60:
                return
            if n == 0:
                res.append("%d:%02d" % (hours, mins))
            for i in range(index, 10):
                if i < 4:
                    dfs(n - 1, hours | (1 << i), mins, i+1, res)
                else:
                    j = i - 4
                    dfs(n - 1, hours, mins | (1 << j), i+1, res)

        res = []
        dfs(num, 0, 0, 0, res)
        return res


# class Solution2:
#     def readBinaryWatch(self, num: int) -> "List[str]":