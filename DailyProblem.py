ans = []
for i in range(1, 9):
    x = i
    for j in range(i+1, 10):
        x = x*10 + j
        if low <= j <= high:
            ans.append(x)
return sorted(ans)
