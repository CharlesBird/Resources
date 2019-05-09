"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 1
        res = 0
        while j <= len(s):
            if j == len(s):
                if s[i] != s[j-1]:
                    res = max(res, j - i)
                else:
                    res = max(res, 1)
            elif s[j] in s[i:j]:
                res = max(res, j - i)
                i = i + s[i:j].index(s[j]) + 1
            j += 1

        # print(res)
        return res



Solution().lengthOfLongestSubstring("aabcbrty")
# Solution().lengthOfLongestSubstring("bbbbb")
# Solution().lengthOfLongestSubstring(" ")
