from typing import List


def combinationSum2(arr: List[int], n: int, target: int) -> List[List[int]]:
    # Write your code here.
    arr.sort()
    res, ans = [], []

    def helper(idx, arr, t, ds, n):
        if t == 0:
            res.append(ds[:])
            return
        if idx == n:
            return
        if arr[idx] <= t:
            ds.append(arr[idx])
            helper(idx+1, arr, t-arr[idx], ds, n)
            ds.pop()
        helper(idx+1, arr, t, ds, n)

    helper(0, arr, target, [], len(arr))
    for i in res:
        if i not in ans:
            ans.append(i)
    return ans

# Link: https://www.codingninjas.com/studio/problems/combination-sum-ii_1112622
