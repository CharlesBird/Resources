"""
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> "List[int]":
        res = []
        # Method 1
        # from collections import Counter
        # cp = Counter(p)
        # cs = Counter(s[:len(p)-1])
        # for i in range(len(p)-1, len(s)):
        #     cs[s[i]] += 1
        #     if cs == cp:
        #         res.append(i-len(p)+1)
        #     cs[s[i-len(p)+1]] -= 1
        #     if cs[s[i-len(p)+1]] == 0:
        #         del cs[s[i-len(p)+1]]
        # Method 2
        pl = [ord(i)-97 for i in p]
        sl = [ord(i)-97 for i in s]
        pi = [0] * 26
        for i in pl:
            pi[i] += 1
        si = [0] * 26
        for i, v in enumerate(sl):
            si[v] += 1
            if i >= len(p):
                si[sl[i-len(p)]] -= 1
            if pi == si:
                res.append(i-len(p)+1)
        print(res)
        return res

Solution().findAnagrams("abab","ab")