def oddEven(N: int) -> str:
    # Write your code here.
    res = N & 1
    if res:
        return "odd"
    return "even"

# Link:https://www.codingninjas.com/studio/problems/odd-even_7993579
