"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to find the smallest set of vertices in a directed acyclic graph


1557. Minimum Number of Vertices to Reach All Nodes

Given a directed acyclic graph, with n vertices numbered from 0 to n-1,
and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable.
It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.



Example 1:
Input: n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
Output: [0,3]
Explanation: It's not possible to reach all the nodes from a single vertex.
From 0 we can reach [0,1,2,5]. From 3 we can reach [3,4,2,5]. So we output [0,3].

Example 2:
Input: n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
Output: [0,2,3]
Explanation: Notice that vertices 0, 3 and 2 are not reachable from any other node, so we must include them.
 Also any of these vertices can reach nodes 1 and 4.


Constraints:
2 <= n <= 10^5
1 <= edges.length <= min(10^5, n * (n - 1) / 2)
edges[i].length == 2
0 <= from[i], to[i] < n
All pairs (from[i], to[i]) are distinct.
"""


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges):
        # Create a boolean list to track whether each node should be included in the result set
        include_list = [True] * n

        # Iterate through each edge in the list
        for i, j in edges:
            # If there is an edge from node i to node j,
            # mark node j as not included in the result set
            include_list[j] = False

        # Return the list of nodes that are marked as included in the result set
        return [i for i in range(n) if include_list[i]]

"""
Intuition
The problem asks us to find the smallest set of vertices from which all nodes in a directed acyclic graph (DAG) are
 reachable. 
 Intuitively, nodes that have no incoming edges are the ones that must be included in the solution set. 
 This is because if a node has no incoming edges, it cannot be reached from any other node in the graph. 
 By identifying these nodes, we can ensure that all other nodes in the graph are reachable.

Approach
To solve the problem, we can use a simple approach:

Create a boolean list, include_list, of length n to track whether each node should be included in the result set. 
Initialize all elements to True.
Iterate through each edge in the given list of edges.
For each edge [i, j], mark the node j as not included in the result set by setting include_list[j] to False.
After processing all edges, return the list of nodes that are marked as included in the result set, 
representing the smallest set of vertices from which all nodes in the graph are reachable.

Complexity
Time complexity:
The time complexity of this approach is O(E), where E is the number of edges in the graph. 
We iterate through each edge once to update the include_list.

Space complexity:
The space complexity is O(N), where N is the number of vertices in the graph. 
The include_list occupies space proportional to the number of vertices.

"""