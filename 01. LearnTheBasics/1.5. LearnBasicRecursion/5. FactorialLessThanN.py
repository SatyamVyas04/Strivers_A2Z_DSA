from typing import *

def factorialNumbers(n: int) -> List[int]:
    l = []
    def recur(num, i, n):
        if num>n:
            return
        l.append(num)
        recur(num*(i+1), i+1, n)
    recur(1, 1, n)
    return l

# Link: https://www.codingninjas.com/studio/problems/factorial-numbers-not-greater-than-n_8365435