from typing import List

def printNos(x: int) -> List[int]:
    l = []
    def recur(i, x):
        if i==0:
            return
        l.append(i)
        recur(i-1, x)
    recur(x, x)
    return l 

# Link: https://www.codingninjas.com/studio/problems/n-to-1-without-loop_8357243