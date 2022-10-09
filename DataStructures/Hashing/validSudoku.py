# Determine if a Sudoku is valid, according to: http://sudoku.com.au/TheRules.aspx
#
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
# The input corresponding to the above configuration :
#
# ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
# A partially filled sudoku which is valid.
#
# Note:
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
#
# A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        n = len(A)
        hmap = {}
        for i in range(n):
            for j in range(n):
                val = str(A[i][j])
                key_row = val + "row" + str(i)  # key for row to check uniqueness
                key_col = val + "col" + str(j)  # key for value to check uniqueness
                key_box = val + "cc" + str(i // 3) + "," + str(j // 3)  # key for box to check uniqueness,
                # i//3 because  3 rows in one box and j//3 because  3 cols in one box

                if val == ".":
                    continue
                if key_row in hmap or key_col in hmap or key_box in hmap:
                    return 0

                hmap[key_row] = str(i) + "row"
                hmap[key_col] = str(j) + "col"
                hmap[key_box] = str(i // 3) + "," + str(j // 3) + "cube"
        return 1
