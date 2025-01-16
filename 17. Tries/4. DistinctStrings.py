from collections import defaultdict

class Trie:
    def __init__(self):
        self.children = defaultdict()   

def countDistinctSubstrings(s):
    cnt = 0
    root = Trie()
    for i in range(len(s)):
        node = root
        for j in range(i, len(s)):
            if s[j] not in node.children:
                cnt += 1
                node.children[s[j]] = Trie()
            node = node.children[s[j]]
    return cnt + 1

# Link: https://www.naukri.com/code360/problems/count-distinct-substrings_985292