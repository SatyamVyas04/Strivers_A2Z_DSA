"""
    Time Complexity : O( N )
    Space complexity: O( 1 )

    Where N is the size of the vehicle array.
"""


from itertools import count


def traffic(n: int, m: int, vehicle: [int]) -> int:
    # Create ans, count and right, and assign with 0.
    ans = 0
    count = 0
    right = 0
    # For loop to move the left pointer.
    for left in range(n):
        # while right is less than n and count is <= m.
        while right < n and count <= m:
            # If vehicle at right is 0.
            if vehicle[right] == 0:
                count += 1
                # Break if count exceeds m.
                if count > m:
                    count -= 1
                    break
            right += 1
        # Update answer.
        ans = max(ans, right - left)
        # If vehicle at left is 0.
        if vehicle[left] == 0:
            count -= 1
    # Return answer.
    return ans

# Link: https://www.codingninjas.com/studio/problems/traffic_6682625