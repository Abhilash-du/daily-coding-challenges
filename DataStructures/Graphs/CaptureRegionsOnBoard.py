"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description:  Capture surrounded regions in a 2-D board of 'X' and 'O' by flipping 'O's into 'X's.

Q3. Capture Regions on Board
Problem Description
Given a 2-D board A of size N x M containing 'X' and 'O', capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Problem Constraints
1 <= N, M <= 1000

Input Format
First and only argument is a N x M character matrix A.

Output Format
Make changes to the the input only as matrix is passed by reference.

Example Input
Input 1:
 A = [
       [X, X, X, X],
       [X, O, O, X],
       [X, X, O, X],
       [X, O, X, X]
     ]
Input 2:
 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]

Example Output
Output 1:  After running your function, the board should be:
 A = [
       [X, X, X, X],
       [X, X, X, X],
       [X, X, X, X],
       [X, O, X, X]
     ]
Output 2: After running your function, the board should be:
 A = [
       [X, O, O],
       [X, O, X],
       [O, O, O]
     ]

Example Explanation
Explanation 1: O in (4,2) is not surrounded by X from below.
Explanation 2: No O's are surrounded.
"""


class Solution:
    # @param A : list of list of chars
    def solve(self, A):

        n = len(A)
        m = len(A[0])
        visited = set()
        dir = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        def dfs(i, j):
            visited.add((i, j))
            for x, y in dir:
                x += i
                y += j
                if -1 < x < n and -1 < y < m and A[x][y] == "O" and (x, y) not in visited:
                    dfs(x, y)

        # Capture 'O' regions starting from the borders
        for i in range(n):
            if A[i][0] == "O" and (i, 0) not in visited:
                dfs(i, 0)
            if A[i][m - 1] == "O" and (i, m - 1) not in visited:
                dfs(i, m - 1)

        for j in range(m):
            if A[0][j] == "O" and (0, j) not in visited:
                dfs(0, j)
            if A[n - 1][j] == "O" and (n - 1, j) not in visited:
                dfs(n - 1, j)

        for i in range(1, n):
            for j in range(1, m):
                if (i, j) not in visited and A[i][j] == "O":
                    A[i][j] = "X"

        return A


"""
Intuition:
The code solves the given problem by performing a depth-first search (DFS) or breadth-first search (BFS) to identify 
the regions surrounded by 'X' in a 2D board.
It starts by capturing the 'O' regions from the borders and marks them as visited. Then, it iterates through the board
 and flips the remaining unvisited 'O' regions to 'X'.

Time Complexity (TC): O(N * M)
The algorithm iterates through the entire N x M board once, 
where N is the number of rows and M is the number of columns.

Space Complexity (SC): O(N * M)
The algorithm uses additional space for the visited set to keep track of visited cells,
 which can consume O(N * M) space in the worst case.



"""