"""
Problem Description
Given an undirected graph having A nodes. A matrix B of size M x 2 is given which represents the edges such that
 there is an edge between B[i][0] and B[i][1].

Find whether the given graph is bipartite or not.
A graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that every edge in
the graph has one node in A and another node in B

Note: There are no self-loops in the graph.

No multiple edges between two pair of vertices.
The graph may or may not be connected.
Nodes are Numbered from 0 to A-1.
Your solution will run on multiple testcases. If you are using global variables make sure to clear them.



Problem Constraints
1 <= A <= 100000
1 <= M <= min(A*(A-1)/2,200000)
0 <= B[i][0],B[i][1] < A



Input Format
The first argument given is an integer A.
The second argument given is the matrix B.

Output Format
Return 1 if the given graph is bipartide else return 0.

Example Input
Input 1:
A = 2
B = [ [0, 1] ]

Input 2:
A = 3
B = [ [0, 1], [0, 2], [1, 2] ]

Example Output
Output 1:1
Output 2:0

Example Explanation
Explanation 1: Put 0 and 1 into 2 different subsets.
Explanation 2: It is impossible to break the graph down to make two different subsets for bipartite matching


"""

from collections import defaultdict, deque

class Solution:
    def solve(self, A, B):
        def BFS(graph, start):
            queue = deque([])  # Create a queue for BFS traversal

            queue.append((start, 1))  # Start BFS from the 'start' node with color 1
            visited[start] = 1  # Mark the 'start' node as visited with color 1

            while queue:
                source, curr_color = queue.popleft()  # Get the source node and its current color
                expected_color = curr_color ^ 1  # Calculate the expected color for adjacent nodes

                for dest in graph[source]:  # Traverse the adjacent nodes of the source node
                    if visited[dest] == -1:  # If the adjacent node is not visited
                        visited[dest] = expected_color  # Mark it as visited with the expected color
                        queue.append((dest, expected_color))  # Add it to the queue for further traversal
                    elif visited[dest] != expected_color:  # If the adjacent node is already visited and its color doesn't match the expected color
                        return False  # The graph is not bipartite

            return True  # All nodes are successfully visited and the graph is bipartite

        graph = defaultdict(list)  # Create an adjacency list to represent the graph

        for left, right in B:  # Iterate over the edges given in matrix B
            graph[left].append(right)  # Add the right node to the adjacency list of the left node
            graph[right].append(left)  # Add the left node to the adjacency list of the right node

        visited = [-1 for _ in range(A + 1)]  # Create a list to track visited nodes and their colors

        for i in range(1, A + 1):  # Iterate over all nodes in the graph
            if visited[i] == -1:  # If the current node is not visited
                visited[i] = 1  # Mark it as visited with color 1
                if not BFS(graph, i):  # Perform BFS from the current node and check if the graph is bipartite
                    return 0  # The graph is not bipartite

        return 1  # The graph is bipartite

"""
Approach:
- We can solve this problem using BFS traversal.
- We will start BFS traversal from each unvisited node and assign it to one of the two sets, A and B, with colors 1 and 0 respectively.
- During the BFS traversal, we will color each node alternately with the expected color based on its parent node.
- If we encounter a visited node that has a color different from the expected color, it means that the graph is not bipartite.
- If we successfully complete the BFS traversal without any conflicts, the graph is bipartite.
- To implement this, we will use an adjacency list to represent the graph and a queue for BFS traversal.
- We will also use a visited array to keep track of visited nodes and their assigned colors.
- We will perform BFS traversal from each unvisited node and check if the graph is bipartite.
- If any BFS traversal detects a conflict, we will return 0, indicating that the graph is not bipartite.
- If all BFS traversals complete without conflicts, we will return 1, indicating that the graph is bipartite.

# Time Complexity:
# - Constructing the adjacency list takes O(M) time,
#   where M is the number of edges in the graph.
# - Performing BFS traversal for each unvisited node takes O(A) time,
#   where A is the number of nodes in the graph.
# - Overall, the time complexity is O(A + M).

# Space Complexity:
# - The space required to store the adjacency list is O(M + A),
#   where M is the number of edges and A is the number of nodes in the graph.
# - The space required for the visited array is O(A).
# - The space required for the queue in BFS traversal is O(A) in the worst case.
# - Therefore, the overall space complexity is O(M + A).


"""
