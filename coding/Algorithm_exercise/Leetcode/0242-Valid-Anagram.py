"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        dict_s = defaultdict(int)
        for i in s:
            dict_s[i] = dict_s[i] + 1
        dict_t = defaultdict(int)
        for i in t:
            dict_t[i] = dict_t[i] + 1
        return dict_s == dict_t