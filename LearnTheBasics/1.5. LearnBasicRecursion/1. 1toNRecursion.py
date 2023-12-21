from typing import List
def printNos(x: int) -> List[int]: 
    l = []
    def recursiveblock(i, x):
        if i>x:
            return
        l.append(i)
        recursiveblock(i+1, x)
    recursiveblock(1, x)
    return l

# Link: https://www.codingninjas.com/studio/problems/print-1-to-n_628290