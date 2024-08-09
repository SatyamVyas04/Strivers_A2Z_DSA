def majorityElement(v: [int]) -> [int]:
    # Write your code here
    d = {}
    ans = []
    mode = len(v) // 3 + 1

    for i in v:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

        if d[i] == mode:
            ans.append(i) 
    
    return sorted(ans)

# Link: https://www.codingninjas.com/studio/problems/majority-element_6915220