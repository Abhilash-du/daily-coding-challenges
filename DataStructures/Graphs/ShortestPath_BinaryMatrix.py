"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
 If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0))
to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected
(i.e., they are different, and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

Examples:-

Example1:
Input: grid = [[0,1],[1,0]]
Output: 2

Example2:
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4

Example3:
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
"""
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        # Check if the start or end cell is blocked
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        # Initialize a queue and enqueue the start cell with distance 1
        q = deque()
        q.append(((0,0), 1))

        # Define the directions for traversal (8-directionally connected cells)
        directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

        while q:
            # Dequeue the current cell and its distance
            current = q.popleft()
            i, j = current[0][0], current[0][1]
            distance = current[1]

            # Check if the destination is reached
            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return distance

            # Explore the neighboring cells
            for dir in directions:
                new_i = i + dir[0]
                new_j = j + dir[1]

                # Check if the neighboring cell is within bounds and unblocked
                if len(grid) > new_i >= 0 == grid[new_i][new_j] and 0 <= new_j < len(grid[0]):
                    # Enqueue the neighboring cell with the updated distance
                    q.append(((new_i, new_j), distance + 1))
                    # Mark the cell as visited by setting it to a non-zero value (1)
                    grid[new_i][new_j] = 1

        # If the destination is not reachable
        return -1


"""
Intuition:
The problem requires finding the shortest clear path from the top-left cell to the bottom-right cell in a binary matrix.
We can use a Breadth-First Search (BFS) algorithm to systematically explore the matrix and find the shortest path.

Time Complexity (TC): O(N^2)
In the worst case, we might need to explore all cells in the matrix, which gives us a time complexity of O(N^2), 
where N is the size of the matrix.

Space Complexity (SC): O(N^2)
We use a queue to store the cells to be explored, which can grow up to N^2 cells in the worst case. 
Hence, the space complexity is O(N^2) due to the queue.
"""