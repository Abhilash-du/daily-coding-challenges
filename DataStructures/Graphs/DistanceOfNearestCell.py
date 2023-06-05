"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine the distance of nearest cell

Q1. Distance of nearest cell

Problem Description
Given a matrix of integers A of size N x M consisting of 0 or 1.
For each cell of the matrix find the distance of nearest 1 in the matrix.
Distance between two cells (x1, y1) and (x2, y2) is defined as |x1 - x2| + |y1 - y2|.
Find and return a matrix B of size N x M which defines for each cell in A distance of nearest 1 in the matrix A.
NOTE: There is at least one 1 is present in the matrix.

Problem Constraints
1 <= N, M <= 1000
0 <= A[i][j] <= 1

Input Format
The first argument given is the integer matrix A.

Output Format
Return the matrix B.

Example Input
Input 1:
 A = [
       [0, 0, 0, 1]
       [0, 0, 1, 1]
       [0, 1, 1, 0]
     ]

Input 2:
 A = [
       [1, 0, 0]
       [0, 0, 0]
       [0, 0, 0]
     ]

Example Output
Output 1:
 [
   [3, 2, 1, 0]
   [2, 1, 0, 0]
   [1, 0, 0, 1]
 ]

Output 2:
 [
   [0, 1, 2]
   [1, 2, 3]
   [2, 3, 4]
 ]


Example Explanation
Explanation 1:
 A[0][0], A[0][1], A[0][2] will be nearest to A[0][3].
 A[1][0], A[1][1] will be nearest to A[1][2].
 A[2][0] will be nearest to A[2][1] and A[2][3] will be nearest to A[2][2].

Explanation 2:
 There is only a single 1. Fill the distance from that 1.

"""
from collections import deque


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        rn = len(A)  # Number of rows in matrix A
        cn = len(A[0])  # Number of columns in matrix A

        visited = [[-1 for _ in range(cn)] for _ in range(rn)]  # Initialize the visited array

        q = deque([])  # Create an empty queue for BFS traversal

        # Traverse the matrix to find cells with value 1 and enqueue them
        for i in range(rn):
            for j in range(cn):
                if A[i][j] == 1:
                    q.append((i, j))  # Enqueue the cell with value 1
                    visited[i][j] = 0  # Mark the cell as visited

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Possible directions for traversal

        # Perform breadth-first search traversal
        while q:
            u, v = q.popleft()  # Dequeue a cell from the queue

            # Traverse in all possible directions
            for x, y in directions:
                x = x + u  # Calculate the new row index
                y = y + v  # Calculate the new column index

                # Check if the new indices are within the matrix boundaries and the cell is not visited yet
                if rn > x > -1 == visited[x][y] and -1 < y < cn:
                    visited[x][y] = visited[u][v] + 1  # Update the distance to the nearest 1
                    q.append((x, y))  # Enqueue the new cell for further traversal

        return visited


"""
Intuition:
The goal of this problem is to find the distance of the nearest 1 for each cell in the matrix. We can use a breadth-first search (BFS) approach to explore the matrix and update the distances accordingly.

Approach:
1. Start by enqueuing all cells with a value of 1 and mark them as visited.
2. Perform a breadth-first search (BFS) traversal by de-queuing cells from the queue.
3. For each dequeued cell, traverse in all possible directions (up, down, left, right).
4. Calculate the new row and column indices based on the current cell and direction.
5. If the new indices are within the matrix boundaries and the cell has not been visited, 
    update the distance to the nearest 1 and enqueue the new cell.
6. Repeat steps 3-5 until the queue is empty.
7. Return the visited array containing the distances.

Time Complexity Analysis:
The time complexity of this solution is O(N * M), where N and M are the dimensions of the input matrix. 
We have to traverse all cells at least once, resulting in a linear time complexity.

Space Complexity Analysis:
The space complexity of this solution is also O(N * M). We use additional space to store the visited array, 
which has the same dimensions as the input matrix. 
Therefore, the space required grows linearly with the size of the matrix.
"""
