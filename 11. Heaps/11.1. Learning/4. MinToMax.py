class Solution:
    def MaxHeapify(self, idx, arr, N):
        left = 2 * idx + 1
        right = 2 * idx + 2
        largest = idx
        if left < N:
            if arr[left] > arr[largest]:
                largest = left
        if right < N:
            if arr[right] > arr[largest]:
                largest = right
        if largest != idx:
            arr[idx], arr[largest] = arr[largest], arr[idx]
            self.MaxHeapify(largest, arr, N)

    def convertMinToMaxHeap(self, N, arr):
        for idx in range(int((N-2)/2), -1, -1):
            self.MaxHeapify(idx, arr, N)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.convertMinToMaxHeap(N, arr)
        for val in arr:
            print(val, end=' ')
        print()

# Link: https://www.geeksforgeeks.org/problems/convert-min-heap-to-max-heap-1666385109/1