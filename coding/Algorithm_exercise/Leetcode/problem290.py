# 290. Word Pattern
"""
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
"""
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        from collections import Counter
        dict_p = Counter(pattern)
        list_s = str.split(' ')
        dict_s = Counter(list_s)
        p_counts = list(dict_p.values())
        s_counts = list(dict_s.values())
        # print(p_counts,s_counts)
        return p_counts==s_counts