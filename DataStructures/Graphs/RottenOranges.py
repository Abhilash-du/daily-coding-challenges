"""
Problem Description
Given a matrix of integers A of size N x M consisting of 0, 1 or 2.

Each cell can have three values:
The value 0 representing an empty cell.
The value 1 representing a fresh orange.
The value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (Left, Right, Top, or Bottom) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.
 If this is impossible, return -1 instead.

Note: Your solution will run on multiple test cases. If you are using global variables, make sure to clear them.

Problem Constraints
1 <= N, M <= 1000
0 <= A[i][j] <= 2

Input Format
The first argument given is the integer matrix A.

Output Format
Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1 instead.

Example Input
Input 1:
A = [   [2, 1, 1]
        [1, 1, 0]
        [0, 1, 1]   ]

Input 2:
A = [   [2, 1, 1]
        [0, 1, 1]
        [1, 0, 1]   ]


Example Output
Output 1: 4
Output 2: -1


Example Explanation
Explanation 1:
Minute 0: [ [2, 1, 1]
            [1, 1, 0]
            [0, 1, 1] ]
Minute 1: [ [2, 2, 1]
            [2, 1, 0]
            [0, 1, 1] ]
Minute 2: [ [2, 2, 2]
            [2, 2, 0]
            [0, 1, 1] ]
Minute 3: [ [2, 2, 2]
            [2, 2, 0]
            [0, 2, 1] ]
Minute 4: [ [2, 2, 2]
            [2, 2, 0]
            [0, 2, 2] ]
At Minute 4, all the oranges are rotten.

Explanation 2: The fresh orange at 2nd row and 0th column cannot be rotten, So return -1.

"""
from collections import deque


class Solution:
    # @param grid : list of list of integers
    # @return an integer
    def solve(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        time = [[-1 for _ in range(cols)] for _ in range(rows)]  # Matrix to store the time required for each cell
        queue = deque([])  # Queue to perform BFS

        # Iterate over the grid and initialize the queue and time matrix
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # Add rotten oranges to the queue with time 0
                    time[i][j] = 0
                if grid[i][j] == 0:
                    time[i][j] = 0  # Mark empty cells with time 0

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Possible directions: right, down, up, left

        # Perform BFS until the queue is empty
        while queue:
            row, col, t = queue.popleft()  # Dequeue the next cell
            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc
                # Check if the new cell is within the bounds of the grid and can be infected
                if new_row > -1 < rows and -1 < new_col < cols and grid[new_row][new_col] != 0 \
                        and time[new_row][new_col] == -1:
                    time[new_row][new_col] = t + 1  # Mark the cell with the current time
                    queue.append((new_row, new_col, t + 1))  # Enqueue the newly infected cell

        max_time = -1  # Initialize the maximum time required to rot an orange
        # Iterate over the time matrix to find the maximum time
        for row in time:
            for val in row:
                if val == -1:
                    return -1  # If there is still a fresh orange, return -1
                max_time = max(max_time, val)  # Update the maximum time

        return max_time  # Return the maximum time required to rot all oranges


'''
Intuition:
- The code solves the problem using a Breadth-First Search (BFS) approach.
- It starts by identifying the initial rotten oranges and marks their timestamps as 0. Empty cells are also marked with timestamp 0.
- Then, it performs a BFS on the grid, updating the timestamps of adjacent fresh oranges to the current timestamp + 1.
- Finally, it finds the maximum timestamp in the grid and returns it as the result.

Time Complexity (TC): O(N * M)
- The BFS algorithm visits each cell at most once, resulting in a time complexity of O(N * M), where N is the number of rows and M is the number of columns in the matrix.

Space Complexity (SC): O(N * M)
- The code utilizes a 2D matrix to store the timestamps for each cell, resulting in a space complexity of O(N * M), where N is the number of rows and M is the number of columns in the matrix.
'''
