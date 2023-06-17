"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine the number of 4-directional walks from the starting square to the ending
, that walk over every non-obstacle square exactly once.

Problem Description
Given a matrix of integers A of size N x M . There are 4 types of squares in it:
1. 1 represents the starting square.  There is exactly one starting square.
2. 2 represents the ending square.  There is exactly one ending square.
3. 0 represents empty squares we can walk over.
4. -1 represents obstacles that we cannot walk over.
Find and return the number of 4-directional walks from the starting square to the ending square,
 that walk over every non-obstacle square exactly once.
Note: Rows are numbered from top to bottom and columns are numbered from left to right.

Problem Constraints
2 <= N * M <= 20
-1 <= A[i] <= 2

Input Format
The first argument given is the integer matrix A.

Output Format
Return the number of 4-directional walks from the starting square to the ending square,
that walk over every non-obstacle square exactly once.

Example Input
Input 1:

A = [   [1, 0, 0, 0]
        [0, 0, 0, 0]
        [0, 0, 2, -1]   ]
Input 2:

A = [   [0, 1]
        [2, 0]    ]


Example Output:-
Output 1: 2
Output 2: 0


Example Explanation:-
Explanation 1:
We have the following two paths:
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Explanation 1:Answer is evident here.
"""


class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        m = len(A[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Possible directions to move
        count = 0  # Counter for the number of paths

        def isValid(u, v):
            """
            Check if the given position (u, v) is valid
            """
            return 0 <= u < n and 0 <= v < m and A[u][v] != -1

        def findPaths(r, c, zeros):
            """
            Recursive function to find all possible paths
            """
            nonlocal count
            if A[r][c] == 2:
                if zeros == 0:  # If all non-obstacle squares are visited
                    count += 1
                return
            temp = A[r][c]
            A[r][c] = -1  # Mark the current square as visited
            for i, j in directions:
                new_r = r + i  # New row index
                new_c = c + j  # New column index
                if isValid(new_r, new_c):
                    findPaths(new_r, new_c, zeros - 1)  # Recursively explore the next valid square
            A[r][c] = temp  # Restore the original value after backtracking

        # Find the count of zeroes and the starting index
        zeros_count = 0
        start_i, start_j = -1, -1
        for i in range(n):
            for j in range(m):
                if A[i][j] == 0:
                    zeros_count += 1
                elif A[i][j] == 1:
                    start_i, start_j = i, j

        if start_i == -1:
            return 0  # No starting square found
        findPaths(start_i, start_j, zeros_count + 1)  # Start the path finding
        return count  # Return the total count of paths
"""
Intuition:
The problem requires finding the number of 4-directional walks from the starting square to the ending square, 
covering every non-obstacle square exactly once.
We can solve this using backtracking, where we explore all possible paths from the starting square to the ending square.
During the exploration, we keep track of the count of paths that cover all non-obstacle squares.

Time Complexity Analysis:
Let N and M be the dimensions of the input matrix.
We explore all possible paths in the matrix, which has a maximum of N * M cells.
Therefore, the time complexity is O(N * M) in the worst case.
Space Complexity Analysis:

The space complexity is determined by the recursive stack during backtracking.
In the worst case, the recursive stack can have a depth of N * M, as we explore all possible paths.
Therefore, the space complexity is O(N * M) in the worst case.
Hope this provides the required explanations!
"""

