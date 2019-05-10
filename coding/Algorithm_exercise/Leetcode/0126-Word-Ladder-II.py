"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

    Only one letter can be changed at a time
    Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

    Return an empty list if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        from collections import defaultdict
        if endWord not in wordList:
            return []
        if beginWord in wordList:
            wordList.remove(beginWord)
        size = len(beginWord)
        res = []
        q = [(beginWord, 1)]
        visited = set()
        all_words_dict = defaultdict(list)
        for word in wordList:
            for i in range(size):
                all_words_dict[word[:i] + '*' + word[i+1:]].append(word)
        mid_res = []
        while q:
            curr_word, step = q.pop(0)

            for i in range(size):
                p_word = curr_word[:i] + '*' + curr_word[i+1:]
                for word in all_words_dict[p_word]:
                    if word == endWord:
                        res.append(mid_res)
                        print(mid_res)
                        return step+1
                    if word not in visited:
                        visited.add(word)
                        q.append((word, step+1))
                all_words_dict[p_word] = []


Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])