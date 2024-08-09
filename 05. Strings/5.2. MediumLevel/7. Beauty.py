from typing import *

def sumOfBeauty(s : str) -> int:
    # Write your code here.
    ans = 0 
    for i in range(len(s)):
        freq = [0]*26
        for j in range(i, len(s)):
            freq[ord(s[j])-97] += 1
            ans += max(freq) - min(x for x in freq if x)
    return ans 

# Link: https://www.codingninjas.com/studio/problems/sum-of-beauty-of-all-substrings_8143656