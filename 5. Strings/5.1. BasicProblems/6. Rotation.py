def isCyclicRotation(A: str, B: str) -> int:
    # Write your code here.
    return int(len(A) == len(B) and B in A + A)

# Link: https://www.codingninjas.com/studio/problems/check-if-one-string-is-a-rotation-of-another-string_1115683