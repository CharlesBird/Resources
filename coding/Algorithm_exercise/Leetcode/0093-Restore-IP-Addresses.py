"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""
class Solution:
    def restoreIpAddresses(self, s: str) -> "List[str]":

        def findIpAddresses(s, index, temp):
            if index == 4:
                if not s:
                    res.append(temp[:-1])
                return
            for i in range(1, 4):
                if i <= len(s):
                    if i == 1:
                        findIpAddresses(s[i:], index+1, temp + s[:i] + ".")
                    elif i == 2 and s[0] != "0":
                        findIpAddresses(s[i:], index + 1, temp + s[:i] + ".")
                    elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                        findIpAddresses(s[i:], index + 1, temp + s[:i] + ".")

        res = []
        if s:
            findIpAddresses(s, 0, "")
        return res