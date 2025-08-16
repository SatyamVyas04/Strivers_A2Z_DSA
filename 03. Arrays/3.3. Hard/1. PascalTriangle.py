def pascalTriangle(n: int) -> list[list[int]]:
    # Write your code here.
    soln = [[1]]
    if n == 1:
        return soln
    for i in range(n-1):
        row = []
        lastrow = soln[-1]
        for i in range(0, len(lastrow)):
            j = i+1
            if j < len(lastrow):
                row.append(lastrow[i] + lastrow[j])
        row.append(1)
        row.insert(0, 1)
        soln.append(row)
    return soln

# Link: https://www.codingninjas.com/studio/problems/print-pascal-s-triangle_6917910
