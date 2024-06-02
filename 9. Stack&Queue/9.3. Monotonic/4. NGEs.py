class Solution:
    def count_NGEs(self, N, arr, queries, indices):
        ans = []
        for idx in indices:
            curr = 0
            for arr_idx in range(idx + 1, N):
                if arr[arr_idx] > arr[idx]:
                    curr += 1
            ans.append(curr)
        return ans

# Link: https://www.geeksforgeeks.org/problems/number-of-nges-to-the-right/1
