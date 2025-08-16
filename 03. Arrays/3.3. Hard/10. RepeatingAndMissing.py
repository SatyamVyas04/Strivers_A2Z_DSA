def findMissingRepeatingNumbers(a: [int]) -> [int]:
    # Write your code here
    n = len(a)
    currsum = sum(a)
    theosum = n*(n+1) // 2
    theosum2 = theosum*(2*n+1) // 3
    currsum2 = 0

    for i in a:
        currsum2 += i**2

    diff = currsum - theosum
    add = (currsum2 - theosum2) // diff
    repeating = (diff + add) // 2
    missing = add - repeating
    return [repeating, missing]

# Link: https://www.codingninjas.com/studio/problems/missing-and-repeating-numbers_6828164
