class TrieNode:
    def __init__(self):
        self.children = {}  # Map-based implementation
        self.v = 0  # Count of words ending at this node
        self.pv = 0  # Count of words passing through this node


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.pv += 1
        cur.v += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self._search(word)
        return 0 if node is None else node.v

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self._search(prefix)
        return 0 if node is None else node.pv

    def erase(self, word: str) -> None:
        cur = self.root
        stack = []
        for c in word:
            if c not in cur.children:
                return  # Word doesn't exist
            stack.append((cur, c))
            cur = cur.children[c]
        cur.v -= 1
        for parent, char in reversed(stack):
            child = parent.children[char]
            child.pv -= 1
            if child.pv == 0:
                del parent.children[char]

    def _search(self, word: str):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return None
            cur = cur.children[c]
        return cur

# Link: https://www.naukri.com/code360/problems/implement-trie_1387095?leftPanelTabValue=SUBMISSION
