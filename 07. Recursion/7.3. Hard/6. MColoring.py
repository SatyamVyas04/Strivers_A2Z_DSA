def graphColoring(mat: list[list[int]], m: int) -> str:
    def solve(node, colors):
        def issafe(currcolor):
            for i in range(totalnodes):
                if i != node and mat[i][node] and colors[i] == currcolor:
                    return False
            return True

        if node == totalnodes:
            return True
        for i in range(m):
            if issafe(i):
                colors[node] = i
                if solve(node + 1, colors):
                    return True
                colors[node] = -1
        return False

    totalnodes = len(mat)
    colors = [-1 for i in range(totalnodes)]
    ans = solve(0, colors)
    if ans:
        return "YES"
    return "NO"

# Link: https://www.codingninjas.com/studio/problems/m-coloring-problem_981273
