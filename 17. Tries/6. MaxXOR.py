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
    def findMaximumXOR(self, nums) -> int:
        trie = Trie()
        for num in nums:
            trie.insert(num)
        ans = 0
        for num in nums:
            ans = max(ans, trie.getmax(num))
        return ans

# Link: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/submissions/1510740334/