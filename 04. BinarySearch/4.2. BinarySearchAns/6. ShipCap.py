def findDays(weights, cap):
    days = 1  # First day
    load = 0
    n = len(weights)  # Size of array
    for i in range(n):
        if load + weights[i] > cap:
            days += 1  # Move to next day
            load = weights[i]  # Load the weight
        else:
            # Load the weight on the same day
            load += weights[i]
    return days


def leastWeightCapacity(weights, d):
    # Find the maximum and the summation
    low = max(weights)
    high = sum(weights)
    while low <= high:
        mid = (low + high) // 2
        numberOfDays = findDays(weights, mid)
        if numberOfDays <= d:
            # Eliminate right half
            high = mid - 1
        else:
            # Eliminate left half
            low = mid + 1
    return low

# Link: https://www.codingninjas.com/studio/problems/capacity-to-ship-packages-within-d-days_1229379
