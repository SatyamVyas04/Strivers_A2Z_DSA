from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_end_of_word = True

    def has_all_prefixes(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.children or not cur.children[char].is_end_of_word:
                return False
            cur = cur.children[char]
        return True


def completeString(n: int, a: List[str]) -> str:
    trie = Trie()

    # Insert all words into the Trie
    for word in a:
        trie.insert(word)

    # Check for the longest complete string
    longest = ""
    for word in a:
        if trie.has_all_prefixes(word):
            # Update longest string if conditions are met
            if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                longest = word

    return longest if longest else "None"

# Link: https://www.naukri.com/code360/problems/complete-string_2687860?leftPanelTabValue=SUBMISSION
