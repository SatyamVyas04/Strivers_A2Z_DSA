import heapq


def minimiseMaxDistance(arr: list[int], k: int) -> float:
    # Write your code here.
    n = len(arr)
    inserted = [0]*(n-1)
    pq = []
    for i in range(0, n-1):
        heapq.heappush(pq, ((arr[i+1] - arr[i]), i))

    for i in range(k):
        dist, index = heapq.nlargest(1, pq)[0]
        pq.remove((dist, index))
        inserted[index] += 1
        inidiff = float(arr[index + 1] - arr[index])
        newseclen = inidiff / float(inserted[index] + 1)
        heapq.heappush(pq, (newseclen, index))

    return heapq.nlargest(1, pq)[0][0]

# Link: https://www.codingninjas.com/studio/problems/minimise-max-distance_7541449
