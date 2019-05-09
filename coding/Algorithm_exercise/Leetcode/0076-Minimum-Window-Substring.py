
"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:

    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter
        dict_t = Counter(t)
        t_char_len = len(dict_t)
        l, r = 0, 0
        s_curr_char_len = 0
        dict_curr_s = {}
        res = float("inf"), None, None
        while r < len(s):
            char = s[r]
            dict_curr_s[char] = dict_curr_s.get(char, 0) + 1
            if char in dict_t and dict_curr_s[char] == dict_t[char]:
                s_curr_char_len += 1
            while l <= r and s_curr_char_len == t_char_len:
                char = s[l]
                if r - l + 1 < res[0]:
                    res = (r - l + 1, l, r)
                dict_curr_s[char] -= 1
                if char in dict_t and dict_curr_s[char] < dict_t[char]:
                    s_curr_char_len -= 1
                l += 1

            r += 1
        return "" if res[0] == float("inf") else s[res[1]:res[2]+1]
