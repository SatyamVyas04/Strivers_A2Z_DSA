from collections import Counter

def sortByFrequency(n: int, s: str) -> str:
    # Write your code here
    c = dict(Counter(s))
    arr = list(zip(c.values(), c.keys()))
    arr.sort()
    ans = ""
    for i in arr:
        ans += i[-1]*i[0]
    return ans

# Link: https://www.codingninjas.com/studio/problems/sorting-characters-by-frequency_1263699