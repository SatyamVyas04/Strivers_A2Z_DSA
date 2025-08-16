from typing import List


def printDivisors(n: int) -> List[int]:
    # Write your code here
    ans = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            ans.append(i)
            if n//i != i:
                ans.append(n//i)
    return sorted(ans)

# Link: https://www.codingninjas.com/studio/problems/print-all-divisors-of-a-number_1164188?leftPanelTabValue=SUBMISSION
