from typing import List

def triplet(n: int, nums: List[int]) -> List[List[int]]:
    # Write your code here.
    res = set()

    # Splitting the input list into negative, positive, and zero lists
    neg, pos, zero = [], [], []
    for i in nums:
        if i > 0:
            pos.append(i)
        elif i < 0:
            neg.append(i)
        else:
            zero.append(i)

    # Converting lists to sets for faster lookups
    N, P = set(neg), set(pos)

    # Case 1: One positive, one negative, and one zero
    if zero:
        for num in P:
            if -num in N:
                res.add((-num, 0, num))

    # Case 2: Three zeros
    if len(zero) >= 3:
        res.add((0, 0, 0))

    # Case 3: Two negatives sum to a positive
    for i in range(len(neg)):
        for j in range(i + 1, len(neg)):
            t = -1 * (neg[i] + neg[j])
            if t in P:
                res.add(tuple(sorted([neg[i], neg[j], t])))

    # Case 4: Two positives sum to a negative
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            t = -1 * (pos[i] + pos[j])
            if t in N:
                res.add(tuple(sorted([pos[i], pos[j], t])))

    # Convert set of tuples to list of lists
    return [list(triplet) for triplet in res]

