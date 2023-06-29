"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine minimum cost of constructing the graph by selecting some given edges such
    that we can reach every other node from the 1st node.

Q2. Construction Cost
Problem Description
Given a graph with A nodes and C weighted edges.
Cost of constructing the graph is the sum of weights of all the edges in the graph.
Find the minimum cost of constructing the graph by selecting some given edges such that we can reach every other node
from the 1st node.
NOTE: Return the answer modulo 109+7 as the answer can be large.

Problem Constraints
1 <= A <= 100000
0 <= C <= 100000
1 <= B[i][0], B[i][1] <= N
1 <= B[i][2] <= 109

Input Format:
First argument is an integer A.
Second argument is a 2-D integer array B of size C*3 denoting edges. B[i][0] and B[i][1] are connected by ith edge with
        weight B[i][2]

Output Format: Return an integer denoting the minimum construction cost.

Example Input
Input 1:

A = 3
B = [   [1, 2, 14]
        [2, 3, 7]
        [3, 1, 2]   ]
Input 2:

A = 3
B = [   [1, 2, 20]
        [2, 3, 17]  ]


Example Output:-
Output 1: 9
Output 2: 37

Example Explanation:-
Explanation 1:
We can take only two edges (2 -> 3 and 3 -> 1) to construct the graph.
we can reach the 1st node from 2nd and 3rd node using only these two edges.
So, the total cost of construction is 9.

Explanation 2: We have to take both the given edges so that we can reach the 1st node from 2nd and 3rd node.

"""
class Solution:
    def solve(self, A, B):
        B.sort(key=lambda x: x[2])  # Sorting the edges by weight
        ans = 0
        MOD = (10 ** 9) + 7
        parent_arr = [i for i in range(A + 1)]  # Initializing parent array for disjoint sets

        def parentOf(node):
            if parent_arr[node] != node:
                parent_arr[node] = parentOf(parent_arr[node])  # Path compression
            return parent_arr[node]

        for nodeA, nodeB, curr_w in B:
            parentA = parentOf(nodeA)
            parentB = parentOf(nodeB)
            if parentA != parentB:
                parent_arr[parentA] = parent_arr[parentB]  # Merge disjoint sets
                ans += curr_w

        return ans % MOD


"""
Intuition: 
We sort the edges in ascending order based on their weights. We use union-find (disjoint set) operations to determine
connected components and merge disjoint sets as needed. 
By iterating over the sorted edges and performing union-find operations, we can find the minimum construction cost of
the graph while ensuring that we can reach every other node from the first node.

# Time Complexity (TC): 
The time complexity is dominated by the sorting operation, which takes O(C log C) time, 
where C is the number of edges. The union-find operations take approximately O(A + C log* A) time, 
where A is the number of nodes and log* represents the iterated logarithm. 
In most cases, the time complexity can be simplified to O(C log C).

# Space Complexity (SC): We use additional space for the parent_arr array, which has a size of A + 1. 
Therefore, the space complexity is O(A).

# Initialize the Solution class and call the solve() function with the required inputs
"""
