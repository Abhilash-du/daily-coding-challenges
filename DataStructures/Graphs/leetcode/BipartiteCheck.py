"""
There is an undirected graph with n nodes, where each node is numbered between 0 and n - 1.
 You are given a 2D array graph, where graph[u] is an array of nodes that node u is adjacent to. More formally,
 for each v in graph[u], there is an undirected edge between node u and node v. The graph has the following properties:

There are no self-edges (graph[u] does not contain u).
There are no parallel edges (graph[u] does not contain duplicate values).
If v is in graph[u], then u is in graph[v] (the graph is undirected).
The graph may not be connected, meaning there may be two nodes u and v such that there is no path between them.
A graph is bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the
graph connects a node in set A and a node in set B.

Return true if and only if it is bipartite.

Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
Output: false
Explanation: There is no way to partition the nodes into two independent sets such that every edge connects a node in
one and a node in the other.

Input: graph = [[1,3],[0,2],[1,3],[0,2]]
Output: true
Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

Constraints:
graph.length == n
1 <= n <= 100
0 <= graph[u].length < n
0 <= graph[u][i] <= n - 1
graph[u] does not contain u.
All the values of graph[u] are unique.
If graph[u] contains v, then graph[v] contains u.
"""
from collections import deque


def isBipartite(self, graph) -> bool:
    n = len(graph)
    # Create a list to store the color of each node
    # 0 means unvisited, 1 means colored as group A, -1 means colored as group B
    colored = [0 for _ in range(n)]

    for node_index in range(n):
        # Skip the node if it has already been colored
        if colored[node_index] != 0:
            continue

        q = deque([node_index])
        # Start coloring the current node as group A
        colored[node_index] = 1

        while q:
            # Process nodes in the queue
            first = q.popleft()
            for node in graph[first]:
                if colored[node] == 0:
                    # Color the adjacent node with the opposite group
                    colored[node] = -colored[first]
                    q.append(node)
                elif colored[node] != -colored[first]:
                    # If the adjacent node is already colored with the same group, the graph is not bipartite
                    return False
    # All nodes have been colored without conflicts, so the graph is bipartite
    return True


"""
# Intuition
To determine if a graph is bipartite, we can color its nodes in two distinct groups such that no two adjacent nodes 
share the same group.

# Approach
1. Initialize a list to store the color of each node. Use 0 to represent unvisited nodes, 1 for nodes in group A, and 
    -1 for nodes in group B.
2. Iterate through each unvisited node in the graph.
3. Perform a breadth-first search (BFS) starting from the current node.
4. During the BFS, color the current node as group A and its adjacent nodes as group B. If an adjacent node is already 
    colored and its color conflicts with the current node's color, return False.
5. If all nodes are colored without conflicts, return True.

# Complexity
- Time complexity:
The time complexity of the solution is O(V + E), where V is the number of vertices (nodes) in the graph and E is the
 number of edges. In the worst case, we need to visit all nodes and edges in the graph.

- Space complexity:
The space complexity is O(V), where V is the number of vertices (nodes) in the graph. We use additional space to store 
the color of each node.
"""
