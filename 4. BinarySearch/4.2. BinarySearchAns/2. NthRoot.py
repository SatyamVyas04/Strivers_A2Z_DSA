def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    low = 1
    high = m
    flag = 1

    while low <= high:
        mid = (low + high) // 2
        flag = 1
        val = 1
        for i in range(n):
            val *= mid
            if val > m:
                flag = 0
                break
        
        if flag == 0:
            high = mid - 1
        elif val == m:
            return mid
        else:
            low = mid + 1
    
    return -1

# Link: https://www.codingninjas.com/studio/problems/nth-root-of-m_1062679