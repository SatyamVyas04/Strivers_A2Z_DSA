from typing import *
from collections import defaultdict


def at_most(s, k):
    if not s:
        return 0
    char_count = {}
    num = 0
    left = 0

    for i in range(len(s)):
        char_count[s[i]] = char_count.get(s[i], 0) + 1
        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                char_count.pop(s[left])
            left += 1
        num += i - left + 1
    return num


def countSubStrings(s: str, k: int) -> int:
    # Write your code here
    return at_most(s, k) - at_most(s, k-1)


# Link: https://www.codingninjas.com/studio/problems/count-with-k-different-characters_1214627
