from typing import List

def generateFibonacciNumbers(n: int) -> List[int]: 
    l = [0, 1]
    size = 2
    for i in range(n-2):
        l.append(l[size-1] + l[size-2])
        size+=1
    return l[:n]

# Link: https://www.codingninjas.com/studio/problems/print-fibonacci-series_7421617