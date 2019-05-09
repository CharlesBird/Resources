"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        res = ''
        list_count_char = [(count, char) for char, count in Counter(s).items()]
        list_count_char.sort(reverse=True)
        for count_char in list_count_char:
            res += count_char[0]*count_char[1]
        # dict_count_s = {}
        # from collections import Counter
        # dict_s = Counter(s)
        # for i in Counter(s):
        #     dict_count_s.setdefault(dict_s[i], []).append(i)
        # res = ''
        # while dict_count_s:
        #     max_count = max(dict_count_s)
        #     for char in dict_count_s[max_count]:
        #         res += char * max_count
        #     del dict_count_s[max_count]
        return res