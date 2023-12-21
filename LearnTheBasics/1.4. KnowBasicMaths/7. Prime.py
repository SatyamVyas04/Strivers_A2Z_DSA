import math
n = int(input())
flag = True
for i in range(2, int(math.sqrt(n)) + 1):
    if n%i == 0:
        flag = False
        break
if flag and n!=1:
    print("YES")
else:
    print("NO")
    
# Link: https://www.codingninjas.com/studio/problems/check-prime_624934