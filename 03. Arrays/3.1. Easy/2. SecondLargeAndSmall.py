def getSecondOrderElements(n: int,  a: list[int]) -> list[int]:
    # Write your code here.
    if n == 2:
        return a
    if n == 3:
        return [sorted(a)[1]]*2
    else:
        a.sort(reverse=True)
        return [a[1], a[-2]]

# Link: https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960
