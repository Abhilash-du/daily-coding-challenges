"""
Problem Description
Given an directed graph having A nodes labelled from 1 to A containing M edges given by matrix B of size M x 2such that
 there is a edge directed from node
B[i][0] to node B[i][1].
Find whether a path exists from node 1 to node A.
Return 1 if path exists else return 0.

NOTE:
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.

Problem Constraints
2 <= A <= 105
1 <= M <= min(200000,A*(A-1))
1 <= B[i][0], B[i][1] <= A

Input Format
The first argument given is an integer A representing the number of nodes in the graph.
The second argument given a matrix B of size M x 2 which represents the M edges such that there is a edge directed from node B[i][0] to node B[i][1].

Output Format
Return 1 if path exists between node 1 to node A else return 0.

Example Input
Input 1:
 A = 5
 B = [  [1, 2]
        [4, 1]
        [2, 4]
        [3, 4]
        [5, 2]
        [1, 3] ]

Input 2:
 A = 5
 B = [  [1, 2]
        [2, 3]
        [3, 4]
        [4, 5] ]

Example Output
Output 1: 0
Output 2: 1

Example Explanation:-
Explanation 1: The given doens't contain any path from node 1 to node 5 so we will return 0.
Explanation 2: Path from node1 to node 5 is ( 1 -> 2 -> 3 -> 4 -> 5 ) so we will return 1.



"""

from collections import deque, defaultdict


class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def solve(self, A, B):

        # Create a defaultdict to store the adjacency list representation of the graph
        graph = defaultdict(list)

        # Build the graph using the input list of edges (B)
        for node1, node2 in B:
            graph[node1].append(node2)

        # Create a deque to implement a queue for BFS traversal
        q = deque()

        # Create a set to keep track of visited nodes
        visited = set()

        # Start BFS traversal from node 1
        q.append(1)
        visited.add(1)

        while q:
            # Get the next node from the queue
            node = q.popleft()

            # Explore all the neighbors of the current node
            for neighbor in graph[node]:
                if neighbor == A:
                    # If the neighbor is the target node (A), return 1
                    return 1

                if neighbor not in visited:
                    # If the neighbor has not been visited, mark it as visited and enqueue it
                    visited.add(neighbor)
                    q.append(neighbor)

        # If the target node (A) is not reachable, return 0
        return 0

"""
Approach:
The given code implements a breadth-first search (BFS) algorithm to check if a target node A is reachable from node 1 
in a graph represented as an adjacency list. The algorithm explores nodes level by level, starting from node 1, 
until it either finds the target node A or exhausts all reachable nodes.

The approach can be summarized as follows:

1. Create a defaultdict to store the adjacency list representation of the graph.
2. Build the graph using the input list of edges (B).
3. Initialize a deque to implement a queue for BFS traversal.
4. Create a set to keep track of visited nodes.
5. Enqueue the starting node 1 and mark it as visited.
6. Perform BFS traversal while the queue is not empty.
   a. Dequeue the next node from the queue.
   b. Explore all the neighbors of the current node.
   c. If the neighbor is the target node A, return 1 (indicating it is reachable).
   d. If the neighbor has not been visited, mark it as visited and enqueue it.
7. If the target node A is not reachable after exploring all reachable nodes, return 0.

Time Complexity:
The time complexity of the BFS algorithm is O(V + E), where V is the number of vertices (A) and E is the number of 
edges (B). In the worst case, the algorithm may need to visit all the nodes and edges in the graph. 
Therefore, the time complexity of the given code is O(V + E).

Space Complexity:
The space complexity of the code is O(V + E) as well. Here, V represents the space required to store the graph 
adjacency list, and E represents the space required for the queue and the visited set. 
In the worst case, all nodes and edges need to be stored, resulting in O(V + E) space complexity.
"""