from typing import List


class Node:
    def __init__(self):
        self.links = [None, None]


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.links[bit] == None:
                node.links[bit] = Node()
            node = node.links[bit]

    def getmax(self, num):
        node = self.root
        max_num = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if node.links[1-bit] != None:
                max_num |= (1 << i)
                node = node.links[1-bit]
            else:
                node = node.links[bit]
        return max_num

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trie = Trie()
        ans = [0] * len(queries)
        queries2 = []
        nums.sort()
        idx = 0
        for query in queries:
            queries2.append((query[1], (query[0], idx)))
            idx += 1
        queries2.sort()
        i = 0
        n = len(nums)
        trie = Trie()
        for end, (start, queryIndex) in queries2:
            while i < n and nums[i] <= end:
                trie.insert(nums[i])
                i += 1
            if i != 0:
                ans[queryIndex] = trie.getmax(start)
            else:
                ans[queryIndex] = -1
        return ans
    
# Link: https://leetcode.com/problems/maximum-xor-with-an-element-from-array/