"""
# Author: Abhilash Dubey
# Problem Statement: ind the shortest distance from C to D and if it is impossible to reach node D from C then return -1.
# GitHub: https://github.com/Abhilash-du/

Problem Description
Given a weighted undirected graph having A nodes, a source node C and destination node D.
Find the shortest distance from C to D and if it is impossible to reach node D from C then return -1.
You are expected to do it in Time Complexity of O(A + M).

Note:
There are no self-loops in the graph.
No multiple edges between two pair of vertices.
The graph may or may not be connected.
Nodes are Numbered from 0 to A-1.
Your solution will run on multiple testcases. If you are using global variables make sure to clear them.

Problem Constraints
1 <= A <= 10^5
0 <= B[i][0], B[i][1] < A
1 <= B[i][2] <= 2
0 <= C < A
0 <= D < A



Input Format:-
The first argument given is an integer A, representing the number of nodes.
The second argument given is the matrix B, where B[i][0] and B[i][1] are connected through an edge of weight B[i][2].
The third argument given is an integer C, representing the source node.
The fourth argument is an integer D, representing the destination node.
Note: B[i][2] will be either 1 or 2.



Output Format: Return the shortest distance from C to D. If it is impossible to reach node D from C then return -1.

Example Input:-
Input 1:
A = 6
B = [   [2, 5, 1]
        [1, 3, 1]
        [0, 5, 2]
        [0, 2, 2]
        [1, 4, 1]
        [0, 1, 1] ]
C = 3
D = 2

Input 2:
A = 2
B = [   [0, 1, 1]
    ]
C = 0
D = 1


Example Output:-
Output 1: 4
Output 2: 1


Example Explanation

Explanation 1:
The path to be followed will be:
    3 -> 1 (Edge weight : 1)
    1 -> 0 (Edge weight : 1)
    0 -> 2 (Edge weight : 2)
Total length of path = 1 + 1 + 2 = 4.

Explanation 2: Path will be 0-> 1.

"""
from collections import defaultdict
import heapq

class Solution:
    def solve(self, A, B, C, D):
        # Construct the graph
        graph = defaultdict(list)
        for source, destination, weight in B:
            graph[source].append((destination, weight))
            graph[destination].append((source, weight))

        # Initialize distance array with infinity
        dist = [float('inf') for _ in range(A)]

        # Set the distance of the source node to 0
        dist[C] = 0

        # Priority queue to store nodes with their corresponding distances
        pq = [(C, 0)]

        # Dijkstra's algorithm
        while pq:
            curr_node, curr_dist = heapq.heappop(pq)

            # If the current distance is greater than the stored distance, skip
            if curr_dist > dist[curr_node]:
                continue

            # Explore neighbors of the current node
            for neighbor, weight in graph[curr_node]:
                # Calculate the potential new distance
                new_dist = curr_dist + weight

                # If the new distance is smaller, update the distance and add to the priority queue
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (neighbor, new_dist))

        # Return the distance to the destination node or -1 if it is unreachable
        return dist[D] if dist[D] != float('inf') else -1


"""
# Step-by-step intuition:

# Construct the graph:
# - The graph is constructed based on the provided edges.
# - Each node is mapped to its neighboring nodes and their corresponding edge weights.

# Initialize distances:
# - The distances are initialized with infinity values for each node except the source node.
# - This prepares the algorithm for finding the shortest path distances.

# Priority queue and exploration:
# - A priority queue is used to explore the nodes in the graph.
# - It starts with the source node and its distance of 0.
# - The priority queue stores nodes and their corresponding distances.

# Dijkstra's algorithm:
# - The algorithm iteratively selects the node with the minimum distance from the priority queue.
# - It checks if the distance to the current node is greater than the stored distance.
#   If it is, the iteration is skipped, as a shorter path to that node has already been found.
# - Otherwise, it explores the neighbors of the current node and calculates the potential new distances.
# - If a new distance is smaller than the stored distance for a neighbor, it updates the distance and adds the neighbor 
    to the priority queue.

# Return the result:
# - After the algorithm finishes, the distances stored for each node represent the shortest path from the source node.
# - If the distance to the destination node is not infinity, it is returned as the shortest path distance.
# - Otherwise, -1 is returned to indicate that the destination node is unreachable from the source node.

----------------------------------
Time Complexity:-
The time complexity of Dijkstra's algorithm depends on the data structure used to implement the priority queue. 
In this case, the algorithm utilizes a priority queue implemented with a min-heap.

In the worst case, each node and edge in the graph will be processed once. 
For each node, the algorithm performs operations such as heap insertion and deletion, which take O(log V) time, 
where V is the number of nodes. For each edge, the algorithm updates the distance, which takes constant time.

Therefore, the overall time complexity of Dijkstra's algorithm with a min-heap priority queue is O((V + E) log V),
 where V is the number of nodes and E is the number of edges. The log V factor arises due to the heap operations in 
 the priority queue.

Space Complexity:-
The space complexity of Dijkstra's algorithm is determined by the data structures used to store the graph and distances.
In this implementation, the graph is stored in a defaultdict of lists, 
which requires O(V + E) space to represent V nodes and E edges.

The dist array stores the shortest distances from the source node to each node. It requires O(V) space.

The priority queue (pq) can contain at most V nodes. Therefore, the space complexity for the priority queue is O(V).

Overall, the space complexity of the algorithm is O(V + E), where V is the number of nodes and E is the number of edges.

In summary:
Time Complexity: O((V + E) log V)
Space Complexity: O(V + E)
"""