"""
Priority Queue in Dijkstra's Algorithm:
- Dijkstra's algorithm uses a priority queue to efficiently select the next node with the smallest tentative distance.
- The priority queue allows the algorithm to always expand the least costly node first, ensuring that the shortest path is found.
- By using a priority queue, the algorithm can maintain a time complexity of O((V + E) log V), where V is the number of vertices and E is the number of edges.
- Without a priority queue, the algorithm would have to search through all nodes to find the smallest tentative distance, resulting in a less efficient O(V^2) time complexity.
"""
