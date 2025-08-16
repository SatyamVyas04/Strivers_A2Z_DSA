n = int(input())

low = 1
high = n
ans = 0

while low <= high:
    mid = (low + high) // 2
    if mid**2 == n:
        ans = mid
        break
    elif mid**2 < n:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)

# Link: https://www.codingninjas.com/studio/problems/square-root-integral_893351
