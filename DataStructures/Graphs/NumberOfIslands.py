"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to find the Number of islands

Problem Description
Given a matrix of integers A of size N x M consisting of 0 and 1. A group of connected 1's forms an island.
From a cell (i, j) such that A[i][j] = 1 you can visit any cell that shares a corner with (i, j) and value
in that cell is 1.

More formally, from any cell (i, j) if A[i][j] = 1 you can visit:

(i-1, j) if (i-1, j) is inside the matrix and A[i-1][j] = 1.
(i, j-1) if (i, j-1) is inside the matrix and A[i][j-1] = 1.
(i+1, j) if (i+1, j) is inside the matrix and A[i+1][j] = 1.
(i, j+1) if (i, j+1) is inside the matrix and A[i][j+1] = 1.
(i-1, j-1) if (i-1, j-1) is inside the matrix and A[i-1][j-1] = 1.
(i+1, j+1) if (i+1, j+1) is inside the matrix and A[i+1][j+1] = 1.
(i-1, j+1) if (i-1, j+1) is inside the matrix and A[i-1][j+1] = 1.
(i+1, j-1) if (i+1, j-1) is inside the matrix and A[i+1][j-1] = 1.
Return the number of islands.

NOTE: Rows are numbered from top to bottom and columns are numbered from left to right.

Problem Constraints
1 <= N, M <= 100
0 <= A[i] <= 1

Input Format
The only argument given is the integer matrix A.

Output Format
Return the number of islands.

Example Input
Input 1:
 A = [
       [0, 1, 0]
       [0, 0, 1]
       [1, 0, 0]
     ]

Input 2:
 A = [
       [1, 1, 0, 0, 0]
       [0, 1, 0, 0, 0]
       [1, 0, 0, 1, 1]
       [0, 0, 0, 0, 0]
       [1, 0, 1, 0, 1]
     ]

Example Output
Output 1: 2
Output 2:5

Example Explanation 1:
 The 1's at position A[0][1] and A[1][2] forms one island.
 Other is formed by A[2][0].

"""

import sys

sys.setrecursionlimit(10 ** 6)
from collections import defaultdict


class Solution:
    # @param A : list of list of integers
    # @return an integer

    def solve(self, A):
        # Determine the number of rows and columns in the matrix
        rows, cols = len(A), len(A[0])

        # Define the eight possible directions to explore from each cell
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        def dfs(i, j):
            # Base cases: check if the cell is out of bounds or contains a 0
            if i < 0 or j < 0 or i >= rows or j >= cols or A[i][j] == 0:
                return

            # Mark the current cell as visited by setting it to 0
            A[i][j] = 0

            # Explore the neighboring cells recursively in all directions
            for dir in directions:
                dfs(i + dir[0], j + dir[1])

            return

        ans = 0
        for rw in range(rows):
            for cl in range(cols):
                if A[rw][cl] == 1:
                    ans += 1
                    dfs(rw, cl)

        return ans


"""
Approach:-
Whenever a cell with unvisited value ‘1’ is encountered we explore all the nodes that are reachable from it and 
continue exploring until no more nodes are left to explore.

While exploring we mark them visited so that no nodes can be explored twice.

After completion of traversal increment the count of islands.

Find for the 1 which is not visited yet.


Time Complexity (TC): The time complexity is determined by the nested loops in the solve() method, which iterate through
 each cell of the matrix. Let's denote the number of rows as N and the number of columns as M. In the worst case, 
 we visit each cell once, resulting in a time complexity of O(N * M).


Space Complexity (SC): The space complexity is primarily determined by the recursive calls made in the dfs() function.
 Since the depth of the recursion is limited by the size of the matrix (N * M), the space complexity is O(N * M) 
 due to the call stack. Additionally, the other variables used in the code have constant space requirements,
  so they do not significantly impact the overall space complexity.

To summarize:
Time Complexity: O(N * M)
Space Complexity: O(N * M)
"""
