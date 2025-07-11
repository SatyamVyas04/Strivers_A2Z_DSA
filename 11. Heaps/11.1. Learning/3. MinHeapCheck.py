class Solution:
    def isMaxHeap(self, arr, n):
        length = len(arr)

        def left(i):
            if 2 * i + 1 < length:
                return arr[2 * i + 1]
            return False

        def right(i):
            if 2 * i + 2 < length:
                return arr[2 * i + 2]
            return False

        for i in range(length):
            if left(i):
                if arr[i] < left(i):
                    return False
            if right(i):
                if arr[i] < right(i):
                    return False
        return True


if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(int(ob.isMaxHeap(arr, n)))

# Link: https://www.geeksforgeeks.org/problems/does-array-represent-heap4345/1