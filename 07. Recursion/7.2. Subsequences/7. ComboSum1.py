from copy import copy, deepcopy


def combSum(candidates, target):
    # Write your code here
    candidates.sort()
    res = []

    def helper(idx, arr, t, ds, n):
        if t == 0:
            res.append(ds[:])
            return
        if idx == n:
            return
        if arr[idx] <= t:
            ds.append(arr[idx])
            helper(idx, arr, t-arr[idx], ds, n)
            ds.pop()
        helper(idx+1, arr, t, ds, n)
    helper(0, candidates, target, [], len(candidates))
    return res

# Link: https://www.codingninjas.com/studio/problems/combination-sum_981296
