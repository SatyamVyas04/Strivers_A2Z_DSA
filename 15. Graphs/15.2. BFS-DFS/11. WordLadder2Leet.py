from collections import deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        if endWord not in wordList:
            return []
        wordList.append(beginWord)
        wordList.append(endWord)
        distance = {}
        self.bfs(endWord, distance, wordList)
        results = []
        self.dfs(beginWord, endWord, distance, wordList, [beginWord], results)
        return results

    def bfs(self, startWord, distance, wordList):
        distance[startWord] = 0
        queue = deque([startWord])
        while queue:
            currentWord = queue.popleft()
            for nextWord in self.get_next_words(currentWord, wordList):
                if nextWord not in distance:
                    distance[nextWord] = distance[currentWord] + 1
                    queue.append(nextWord)

    def get_next_words(self, word, wordList):
        nextWords = []
        for i in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                nextWord = word[:i] + char + word[i + 1:]
                if nextWord != word and nextWord in wordList:
                    nextWords.append(nextWord)
        return nextWords

    def dfs(self, currentWord, targetWord, distance, wordList, path, results):
        if currentWord == targetWord:
            results.append(list(path))
            return

        for nextWord in self.get_next_words(currentWord, wordList):
            try:
                if distance[nextWord] != distance[currentWord] - 1:
                    continue
            except KeyError:
                return
            path.append(nextWord)
            self.dfs(nextWord, targetWord, distance, wordList, path, results)
            path.pop()

# Link: https://leetcode.com/problems/word-ladder-ii/
