from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        queue = deque([(beginWord, 1)])
        wordList = set(wordList)

        while queue:
            currword, level = queue.popleft()
            if currword == endWord and level != 1:
                return level
            for index in range(len(currword)):
                for i in range(97, 123):
                    ch = chr(i)
                    newword = currword[:index] + ch + currword[index+1:]
                    if wordList.__contains__(newword):
                        wordList.remove(newword)
                        queue.append((newword, level + 1))
        return 0

# Link: https://leetcode.com/problems/word-ladder/