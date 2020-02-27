"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [False] * (n + 1)

        def helper(s, index):
            print(memo)
            if index == len(s):
                return True

            if memo[index]:
                return memo[index]

            for i in range(index, len(s) + 1):
                if s[index:i] in wordDict:
                    memo[i] = helper(s, i)
                    if memo[i]:
                        return True

            return False

        return helper(s, 0)


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def isindict(s, my_dict):
            if s in my_dict or not s:
                return True
            else:
                for word in my_dict:
                    if word in s:
                        left, right = s.split(word, 1)
                        if left in dp:left_result = dp[left]
                        else:
                            left_result = isindict(left, my_dict)
                            dp[left] = left_result
                        if right in dp:right_result = dp[right]
                        else:
                            right_result = isindict(right, my_dict)
                            dp[right] = right_result
                        if left_result and right_result:
                            return True
            return False
        return isindict(s, wordDict)


class Solution3:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Time Complexity: O(len(s)*len(s))
        # Space Complexity: O(len(s))
        n = len(s)
        dp = [False] * (n + 1)

        dp[0] = True

        for i in range(n):
            if dp[i]:
                for j in range(i, n):
                    if s[i:j + 1] in wordDict:
                        dp[j + 1] = True

        return dp[n]


s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
res = Solution().wordBreak(s, wordDict)
print(res)