"""
Problem Description
Write a program to solve a Sudoku puzzle by filling the empty cells. Empty cells are indicated by the character '.'
You may assume that there will be only one unique solution.

Problem Constraints
N = 9

Input Format
First argument is an array of array of characters representing the Sudoku puzzle.

Output Format
Modify the given input to the required answer.

Example Input
Input 1:
A = [[53..7....], [6..195...], [.98....6.], [8...6...3], [4..8.3..1], [7...2...6], [.6....28.], [...419..5], [....8..79]]

Example Output:-
Output 1:-
[[534678912], [672195348], [198342567], [859761423], [426853791], [713924856], [961537284], [287419635], [345286179]]

Example Explanation:-
Explanation 1: Look at the diagrams given in the question.
"""


class Solution:
    # @param A : list of list of chars
    def solveSudoku(self, mat):
        def isValueValid(val, row, col):
            # Check if the value is already present in the same row or column
            for i in range(9):
                if mat[row][i] == val or mat[i][col] == val:
                    return False

            # Find the starting indices of the corresponding 3x3 subgrid
            start_row = row - (row % 3)
            start_col = col - (col % 3)

            # Check if the value is already present in the subgrid
            for i in range(3):
                for j in range(3):
                    if val == mat[i + start_row][j + start_col]:
                        return False
            return True

        def solveSudokuHelper(cellNo):
            # Base case: If all cells have been filled, the puzzle is solved
            if cellNo == 81:
                return True

            row = cellNo // 9
            col = cellNo % 9

            # If the cell is already filled, move to the next cell
            if mat[row][col] != ".":
                return solveSudokuHelper(cellNo + 1)

            # Try placing values from 1 to 9 in the cell and recursively solve
            for value in range(1, 10):
                val = str(value)
                if isValueValid(val, row, col):
                    mat[row][col] = val
                    if solveSudokuHelper(cellNo + 1):
                        return True
                    else:
                        mat[row][col] = "."
            return False

        solveSudokuHelper(0)
        return mat


"""
Intuition:
The Sudoku puzzle is solved using a backtracking algorithm.
The solveSudoku function takes the Sudoku puzzle as input and modifies it in-place to fill the empty cells.
The algorithm starts with the first cell and tries placing values from 1 to 9 in the empty cells.
It uses the isValueValid helper function to check if a value can be placed in a particular cell 
    without violating the Sudoku rules.
If a value is valid, it is placed in the cell, and the algorithm moves to the next cell.
If all cells are filled without any violations, the puzzle is solved.
If a violation occurs or the algorithm reaches the end of the puzzle without finding a solution, 
    it backtracks to the previous cell and tries a different value.
This process continues until a valid solution is found or all possibilities are exhausted.

Time Complexity:
The time complexity of the algorithm is O(9^(n*n)), where n is the size of the Sudoku grid.
In the worst case, each empty cell can have 9 possible values to try.
However, due to the constraint of a unique solution, the actual number of recursive calls is much lower.

Space Complexity:
The space complexity of the algorithm is O(n*n) for the Sudoku grid, as the input grid is modified in-place.
The recursive calls also require O(n*n) space for the call stack.
"""
