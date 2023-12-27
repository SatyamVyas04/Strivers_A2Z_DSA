class Solution:
    def subarraySum(self, arr: [int], k: int) -> int:
        hashmap = {}
        hashmap[0] = 1
        pre, count = 0, 0
        for i in arr:
            pre += i
            remove = pre - k
            if remove in hashmap.keys():
                count += hashmap[remove]
                
            if pre in hashmap:
                hashmap[pre] += 1
            else:
                hashmap[pre] = 1
        
        return count 
    
# Link: https://leetcode.com/problems/subarray-sum-equals-k/