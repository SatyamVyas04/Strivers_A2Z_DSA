'''
    Time Complexity: O((N + M))
    Space Complexity: O(N + M)

    N and M are the sizes of array 'A' and 'B' respectively.
'''

def sortedArray(a: [int], b: [int]) -> [int]:

    # return sorted(list(set(a).union(set(b))))

    n = len(a)
    m = len(b)
    # Dynamic Array to store the union of 'a' and 'b'
    unionArray = []

    i = 0
    j = 0
    # Iterating over both arrays
    while (i < n and j < m):

        # Current element in a is smaller or
        # equal to the current element in b
        if (a[i] <= b[j]):

            # Checking whether same element
            # exists in the 'unionArray' or not.
            if (len(unionArray) == 0 or
                    unionArray[-1] != a[i]):
                unionArray.append(a[i])

            # Incrementing i
            i += 1
        else:
            # A[i] > B[j]
            if (len(unionArray) == 0 or
                    unionArray[-1] != b[j]):
                unionArray.append(b[j])

            # Incrementing j
            j += 1
    # Traversing over 'a' to insert
    # elements which are left
    while (i < n):
        if (unionArray[-1] != a[i]):
            unionArray.append(a[i])

        # Incrementing i
        i += 1

    # Traverse over 'b' to insert
    # elements which are left
    while (j < m):
        if (unionArray[-1] != b[j]):
            unionArray.append(b[j])

        # Incrementing j
        j += 1

    return unionArray

# Link: https://www.codingninjas.com/studio/problems/sorted-array_6613259