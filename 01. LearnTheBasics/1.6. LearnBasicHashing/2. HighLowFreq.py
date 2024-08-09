from typing import List
from collections import Counter

def getFrequencies(v: List[int]) -> List[int]: 
    # Write your code here
    c = Counter(v)
    setkeys = set(c.keys())
    maxval = max(c.values())
    minval = min(c.values())
    maxkeys = []
    minkeys = []
    for i in c.keys():
        if c[i] == maxval:
            maxkeys.append(i)
        if c[i] == minval:
            minkeys.append(i)
        
    return min(maxkeys), min(minkeys)
    
# Link: https://www.codingninjas.com/studio/problems/k-most-occurrent-numbers_625382