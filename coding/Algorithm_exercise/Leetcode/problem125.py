# 125. Valid Palindrome
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        # s = ''.join(re.findall(r'\w+', s.lower()))
        # s = re.sub('[^A-Za-z0-9]', '', s).lower()
        s = ''.join(re.split(r'[^A-Za-z0-9]', s)).lower()
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

res=Solution().isPalindrome('A man, a plan, a canal: Panama')
print(res)