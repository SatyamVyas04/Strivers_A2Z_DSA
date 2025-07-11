from collections import defaultdict
from heapq import heappop, heapify


class Solution:
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        l = len(hand)
        if l % W:
            return False
        if W == 1:
            return True

        # first we count the numbers
        cnt = defaultdict(int)
        for i in hand:
            cnt[i] += 1
        # then we build the minimum heap
        heapify(hand)

        for i in range(l // W):
            # first we find the starting number of current group
            start = heappop(hand)
            while cnt[start] == 0:  # if the number is no loner available
                start = heappop(hand)  # we pop again

            # Now we find the all other numbers in the group
            for i in range(W):
                cnt[start] -= 1  # decrease its counts
                if cnt[start] < 0:  # the number is not available
                    return False
                start += 1
        return True

# Link: https://leetcode.com/problems/hand-of-straights/