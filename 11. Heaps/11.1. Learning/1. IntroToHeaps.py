H = [0] * 10009
s = -1


def parent(i):
    return (i - 1) // 2


def leftChild(i):
    return 2 * i + 1


def rightChild(i):
    return 2 * i + 2


def shiftUp(i):
    while i > 0 and H[parent(i)] < H[i]:
        H[parent(i)], H[i] = H[i], H[parent(i)]
        i = parent(i)


def shiftDown(i):
    maxIndex = i
    l = leftChild(i)
    if l <= s and H[l] > H[maxIndex]:
        maxIndex = l
    r = rightChild(i)
    if r <= s and H[r] > H[maxIndex]:
        maxIndex = r
    if (i != maxIndex):
        H[i], H[maxIndex] = H[maxIndex], H[i]
        shiftDown(maxIndex)


def insert(p):
    global s
    s += 1
    H[s] = p
    shiftUp(s)


class Solution:
    def extractMax(self):
        global s
        if H:
            res = H[0]
            H[0] = H[s]
            s -= 1
            shiftDown(0)
        return res


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        for val in a:
            insert(val)
        ob = Solution()
        print('Node with maximum priority :', ob.extractMax())
        print('Priority queue after extracting maximum : ', end='')
        for i in range(s + 1):
            print(H[i], end=' ')
        print()


# Link: https://www.geeksforgeeks.org/problems/implementation-of-priority-queue-using-binary-heap/