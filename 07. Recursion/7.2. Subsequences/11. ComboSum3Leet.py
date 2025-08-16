class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ansarr = []

        def helper(arr, idx, ds):
            if len(ds) == k:
                if sum(ds) == n:
                    ansarr.append(sorted(ds))
                return
            if idx >= len(arr):
                return

            ds.append(arr[idx])
            helper(arr, idx + 1, ds)
            ds.pop()
            helper(arr, idx + 1, ds)

        helper([i for i in range(1, 10)], 0, [])

        return sorted(ansarr)

# Link: https://leetcode.com/problems/combination-sum-iii/
