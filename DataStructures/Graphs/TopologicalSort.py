"""
Problem Description
Given an directed acyclic graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such
that there is a edge directed from node B[i][0] to node B[i][1].

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed
edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

Return the topological ordering of the graph and if it doesn't exist then return an empty array.

If there is a solution return the correct ordering. If there are multiple solutions print the lexographically smallest one.

Ordering (a, b, c) is said to be lexographically smaller than ordering (e, f, g) if a < e or if(a==e) then b < f and so on.

NOTE:

There are no self-loops in the graph.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.


Problem Constraints
2 <= A <= 104

1 <= M <= min(100000,A*(A-1))

1 <= B[i][0], B[i][1] <= A



Input Format
The first argument given is an integer A representing the number of nodes in the graph.
The second argument given a matrix B of size M x 2 which represents the M edges such that there is a edge directed
from node B[i][0] to node B[i][1].

Output Format
Return a one-dimensional array denoting the topological ordering of the graph
and if it doesn't exist then return empty array.

Example Input:-

Input 1:
 A = 6
 B = [  [6, 3]
        [6, 1]
        [5, 1]
        [5, 2]
        [3, 4]
        [4, 2] ]

Input 2:
 A = 3
 B = [  [1, 2]
        [2, 3]
        [3, 1] ]

Example Output
Output 1: [5, 6, 1, 3, 4, 2]
Output 2: []

Example Explanation:-
Explanation 1: The given graph contain no cycle so topological ordering exists which is [5, 6, 1, 3, 4, 2]
Explanation 2: The given graph contain cycle so topological ordering not possible we will return empty array.

"""
from collections import defaultdict
import heapq as pq


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, N, Arr):
        graph = defaultdict(list)  # Adjacency list to represent the graph
        inorder = defaultdict(int)  # Keep track of the in-degree of each node
        min_heap = []  # Priority queue (min-heap)

        # Build the graph and count the in-degree of each node
        for f, t in Arr:
            graph[f].append(t)
            inorder[t] += 1

        # Initialize the min-heap with nodes having in-degree 0
        for node in range(1, N + 1):
            if inorder[node] == 0:
                pq.heappush(min_heap, node)

        ans = []  # Resultant list to store the topological ordering

        # Perform topological sorting using min-heap
        while min_heap:
            curr_node = pq.heappop(min_heap)  # Pop the node with the minimum in-degree
            ans.append(curr_node)  # Add the current node to the result

            # Decrement the in-degree of each child node and push nodes with in-degree 0 to the min-heap
            for child in graph[curr_node]:
                inorder[child] -= 1
                if inorder[child] == 0:
                    pq.heappush(min_heap, child)

        return ans


"""
Intuition:
- Build a directed graph using the given edges (Arr) and count the in-degree of each node.
- Start with the nodes having in-degree 0 and perform topological sorting using a min-heap.
- In each iteration, pop a node from the min-heap, add it to the result, and decrement the in-degree of its child nodes.
- If a child node's in-degree becomes 0, push it into the min-heap.
- Repeat until the min-heap is empty.
- If all nodes are visited during the process, return the resultant topological ordering. Otherwise,
 return an empty array.

Time Complexity (TC):
- Building the graph takes O(M) time, where M is the number of edges.
- Performing topological sorting takes O(N + M) time, as each node is processed once and each edge is traversed once.
- Therefore, the overall time complexity is O(N + M).

Space Complexity (SC):
- The space complexity is O(N + M) since we are using a defaultdict and a min-heap to store the graph and 
intermediate results.

"""
