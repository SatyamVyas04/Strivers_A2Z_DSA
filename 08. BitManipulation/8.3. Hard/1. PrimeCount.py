def countPrimes(n: int) -> list[int]:
    def prime(x):
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for i in range(3, int(x**0.5)+1, 2):
            if x % i == 0:
                return False
        return True

    ans = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 and prime(i):
            ans.append(i)
        if n//i != i and prime(n//i) and n % i == 0:
            ans.append(n//i)
    return ans

# Link: https://www.codingninjas.com/studio/problems/prime-factorisation_1760849?leftPanelTabValue=SUBMISSION
