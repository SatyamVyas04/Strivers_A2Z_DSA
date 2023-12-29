def triplet(n: int, nums: [int]) -> [[int]]:
    # Write your code here.
    res = set()

    # Spliting
    n, p, z = [], [], []
    for i in nums:
        if i>0:
            p.append(i)
        elif i<0:
            n.append(i)
        else:
            z.append(i)

    N, P = set(n), set(p)

    # Case1: p, 1z, n
    if z:
        for num in P:
            if -1*num in N:
                res.add((-1*num, 0, num))

    
    # Case2: 0, 0, 0
    if len(z)>=3:
        res.add((0,0,0))

    # Case 3: 2 negatives == 1 positive
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            t = -1*(n[i] + n[j])
            if t in P:
                res.add(tuple(sorted([n[i], n[j], t])))

    # Case 4: 2 positive == 1 negative
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            t = -1*(p[i] + p[j])
            if t in N:
                res.add(tuple(sorted([p[i], p[j], t])))

    return list(map(list, res))

# Link: https://www.codingninjas.com/studio/problems/three-sum_6922132

# Optimal Approach
# def triplet(n, arr):
#     ans = []
#     arr.sort()
#     for i in range(n):
#         # remove duplicates:
#         if i != 0 and arr[i] == arr[i - 1]:
#             continue

#         # moving 2 pointers:
#         j = i + 1
#         k = n - 1
#         while j < k:
#             total_sum = arr[i] + arr[j] + arr[k]
#             if total_sum < 0:
#                 j += 1
#             elif total_sum > 0:
#                 k -= 1
#             else:
#                 temp = [arr[i], arr[j], arr[k]]
#                 ans.append(temp)
#                 j += 1
#                 k -= 1
#                 # skip the duplicates:
#                 while j < k and arr[j] == arr[j - 1]:
#                     j += 1
#                 while j < k and arr[k] == arr[k + 1]:
#                     k -= 1

#     return ans


# arr = [-1, 0, 1, 2, -1, -4]
# n = len(arr)
# ans = triplet(n, arr)
# for it in ans:
#     print("[", end="")
#     for i in it:
#         print(i, end=" ")
#     print("]", end=" ")
# print()