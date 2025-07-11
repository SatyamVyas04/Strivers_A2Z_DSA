class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
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

# Link: https://leetcode.com/problems/combination-sum/