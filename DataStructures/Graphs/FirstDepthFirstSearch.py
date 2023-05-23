"""
Problem Description
You are given N towns (1 to N). All towns are connected via unique directed path as mentioned in the input.
Given 2 towns find whether you can reach the first town from the second without repeating any edge.
B C : query to find whether B is reachable from C.
Input contains an integer array A of size N and 2 integers B and C ( 1 <= B, C <= N ).
There exist a directed edge from A[i] to i+1 for every 1 <= i < N.
 Also, it's guaranteed that A[i] <= i for every 1 <= i < N.
NOTE: Array A is 0-indexed. A[0] = 1 which you can ignore as it doesn't represent any edge.

Problem Constraints
1 <= N <= 100000

Input Format
First argument is vector A
Second argument is integer B
Third argument is integer C

Output Format
Return 1 if reachable, 0 otherwise.

Example Input
Input 1:
 A = [1, 1, 2]
 B = 1
 C = 2

Input 2:
 A = [1, 1, 2]
 B = 2
 C = 1

Example Output
Output 1: 0
Output 2: 1

Example Explanation
Explanation 1: Tree is 1--> 2--> 3 and hence 1 is not reachable from 2.
Explanation 2: Tree is 1--> 2--> 3 and hence 2 is reachable from 1.
"""
from collections import defaultdict


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        n = len(A)
        adj_list = defaultdict(list)

        # Create adjacency list representation of the graph
        for i in range(1, n):
            adj_list[A[i]].append(i + 1)

        def dfs(adj_list, src, dest):
            # Base case: if source node equals destination node, return 1 (path found)
            if src == dest:
                return 1

            # Recursive depth-first search
            for val in adj_list[src]:
                if dfs(adj_list, val, dest):
                    return 1

            return 0  # Return 0 if no path found

        return dfs(adj_list, C, B)

"""
Intuition:
The problem can be approached by traversing the directed edges of the towns. We need to check if we can reach town B 
from town C without repeating any edge.

Approach:
1. Create an adjacency list representation of the directed graph using the input array A.
2. Implement a depth-first search (DFS) algorithm to traverse the graph and check if town B is reachable from town C.
3. Start the DFS from town C and recursively visit the neighboring towns.
4. Keep track of the visited towns to avoid revisiting the same town.
5. If town B is found during the DFS traversal, return 1 (reachable). Otherwise, return 0 (not reachable).

Complexity
Time complexity: O(N), where N is the number of towns. We need to traverse all the towns to build the adjacency list 
and perform the DFS traversal.

Space complexity: O(N), as we need to store the adjacency list and maintain a visited array to track the visited towns 
during DFS.
"""