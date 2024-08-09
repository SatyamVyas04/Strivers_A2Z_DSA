class Solution:
    def nextPermutation(self, arr: [int]) -> None:
        ptr = -1
        n = len(arr)
        flag = 0

        for i in range(n-2, -1, -1):
            if arr[i] < arr[i+1]:
                ptr = i
                flag = 1
                break

        if flag == 0 and ptr == -1:
            arr[:] = arr[::-1]

        if flag:  
            for j in range(n-1, ptr, -1):
                if arr[j] > arr[ptr]:
                    arr[j], arr[ptr] = arr[ptr], arr[j]
                    break
            
            arr[:] = arr[:ptr+1] + arr[ptr+1:][::-1]

# Link: https://leetcode.com/problems/next-permutation/