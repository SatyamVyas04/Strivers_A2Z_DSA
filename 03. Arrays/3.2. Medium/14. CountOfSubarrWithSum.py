from os import *
from sys import *
from collections import *
from math import *

def findAllSubarraysWithGivenSum(arr, k):
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

# Link: https://www.codingninjas.com/studio/problems/subarray-sums-i_1467103