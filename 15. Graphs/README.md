# Overview

## 15.1. Graph Introduction

One of the most important data structures. Graphs are everywhere, from social networks to transportation systems. This section covers the basics of graph representation, including adjacency lists and matrices, as well as fundamental algorithms like Depth-First Search (DFS) and Breadth-First Search (BFS). Graph traversal techniques are essential for exploring and analyzing graph structures. These are asked extensively in interviews and competitive programming contests.

## 15.2. BFS and DFS Applications

BFS and DFS are widely used for various applications, including:

- Finding the shortest path in unweighted graphs (BFS)
- Detecting cycles in graphs (DFS)
- Topological sorting of directed acyclic graphs (DFS)
- Solving puzzles and games (BFS)
- Network broadcasting (BFS)

Understanding these applications is crucial for leveraging graph algorithms effectively.

## 15.3. Topological Sorting

Topological sorting is a linear ordering of vertices in a directed acyclic graph (DAG) such that for every directed edge (u, v), vertex u comes before vertex v in the ordering. This is particularly useful in scenarios like task scheduling, where certain tasks must be completed before others can begin. The two primary algorithms for topological sorting are Kahn's algorithm (BFS-based) and DFS-based approach. Kahn's algorithm uses in-degree of vertices to determine the order, while the DFS-based approach relies on post-order traversal.

## 15.4. Shortest Path Algorithms

This section covers algorithms for finding the shortest path in graphs, including:

- Dijkstra's Algorithm: Efficient for graphs with non-negative weights.
- Bellman-Ford Algorithm: Handles graphs with negative weights and detects negative cycles.
- Floyd-Warshall Algorithm: Computes shortest paths between all pairs of vertices.

## 15.5. MST and Disjoint Set

Prim's and Kruskal's algorithms are covered for finding the Minimum Spanning Tree (MST) of a graph. The Disjoint Set Union (DSU) or Union-Find data structure is also discussed, which is essential for Kruskal's algorithm and helps manage and merge sets efficiently.

## Important Questions

| Topic | Rating | Question             | Solution Link                                              | Date              |
| :---- | :----- | :------------------- | :--------------------------------------------------------- | :---------------- |
| Graph | Easy   | Connect Provinces    | [Here](./15.2.%20BFS-DFS/1.%20ConnectedProvinces.py)       | 16th August 2024  |
| Graph | Medium | Surrounded Regions   | [Here](./15.2.%20BFS-DFS/8.%20SurroundedRegionsLeet.py)    | 3rd January 2025  |
| Graph | Medium | Word Ladder          | [Here](./15.2.%20BFS-DFS/10.%20WordLadder1Leet.py)         | 3rd January 2025  |
| Graph | Medium | Course Schedule      | [Here](./15.3.%20Topo-Sort/4.%20CourseScheduleLeet1.py)    | 5th January 2025  |
| Graph | Medium | Cheapest Flights     | [Here](./15.4.%20ShortestPath/7.%20CheapestFlightsLeet.py) | 8th January 2025  |
| Graph | Medium | Bellman Ford         | [Here](./15.4.%20ShortestPath/11.%20BellmanFord.py)        | 9th January 2025  |
| Graph | Medium | Floyd Warshall       | [Here](./15.4.%20ShortestPath/12.%20FloydWarshal.py)       | 9th January 2025  |
| Graph | Hard   | Network Connection   | [Here](./15.5.%20MST-Disjoint/6.%20NetworkConnLeet.py)     | 10th January 2025 |
| Graph | Hard   | Remove Stones        | [Here](./15.5.%20MST-Disjoint/7.%20RowColStonesLeet.py)    | 10th January 2025 |
| Graph | Hard   | Swim in Rising Water | [Here](./15.5.%20MST-Disjoint/11.%20RisingWaterLeet.py)    | 10th January 2025 |

## That's it :)

```plaintext
आत्मौपम्येन सर्वत्र
समं पश्यति योऽर्जुन ।
सुखं वा यदि वा दुःखं
स योगी परमो मतः ॥

6.32
```

> The yogi who treats all beings as equal, seeing their joys and sorrows as his own, is considered the highest yogi.
