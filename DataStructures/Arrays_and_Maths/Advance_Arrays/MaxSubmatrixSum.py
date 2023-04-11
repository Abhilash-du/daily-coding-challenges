# Problem Description
# Given a row-wise and column-wise sorted matrix A of size N * M.
# Return the maximum non-empty submatrix sum of this matrix.
#
# Problem Constraints
# 1 <= N, M <= 1000
# -10^9 <= A[i][j] <= 10^9
#
# Input Format: The first argument is a 2D integer array A.
#
# Output Format: Return a single integer that is the maximum non-empty submatrix sum of this matrix.
#
# Example Input
# Input 1:-
#     -5 -4 -3
# A = -1  2  3
#      2  2  4
# Input 2:-
#     1 2 3
# A = 4 5 6
#     7 8 9
#
# Example Output
# Output 1:12
# Output 2: 45
#
#
# Example Explanation
# Expanation 1:-
# The submatrix with max sum is
# -1 2 3
#  2 2 4
#  Sum is 12.
# Explanation 2:-
# The largest submatrix with max sum is
# 1 2 3
# 4 5 6
# 7 8 9
# The sum is 45.

class Solution:
    # @param A : list of integers
    # @return a long
    def solve(self, A):
        r = len(A) + 1
        c = len(A[0]) + 1

        prefix_arr = [[0 for _ in range(c)] for __ in range(r)]

        for rw in range(1, r):
            for col in range(1, c):
                prefix_arr[rw][col] = prefix_arr[rw][col - 1] + prefix_arr[rw - 1][col] + A[rw - 1][col - 1] - \
                                      prefix_arr[rw - 1][col - 1]

        max_sum = prefix_arr[r - 1][c - 1]
        fixed_end = prefix_arr[r - 1][c - 1]
        for row in range(1, r):
            for col in range(1, c):
                if row == 1 and col == 1:
                    continue
                curr_sum = fixed_end - prefix_arr[r - 1][col - 1] - prefix_arr[row - 1][c - 1] + prefix_arr[row - 1][
                    col - 1]
                max_sum = max(curr_sum, max_sum)

        return max_sum
#
# Solution Approach:-
# The given code implements a solution to find the maximum sum of submatrix in a given matrix A.
#
# Approach:
# The solution uses prefix sum technique to calculate the sum of submatrix for each possible submatrix.
# It initializes a prefix array of size (n+1) x (m+1) where n is the number of rows and m is the number of columns
# in the matrix A. The prefix array is initialized with all elements as zero.
# Then, it fills the prefix array with cumulative sum for each element of A.
#
# In other words, for each (i,j) position in A, p
# refix_arr[i][j] = A[i-1][j-1] + prefix_arr[i-1][j] + prefix_arr[i][j-1] - prefix_arr[i-1][j-1].
# This formula is used to fill the prefix array.
#
# After the prefix array is filled, it then calculates the sum of submatrix for each submatrix.
# For each submatrix, it calculates the sum using the formula :-
#
# curr_sum=fixed_end-prefix_arr[r-1][col-1]-prefix_arr[row-1][c-1]+prefix_arr[row-1][col-1].
#
# It keeps track of the maximum sum found so far.
#
# The time complexity of the solution is O(n^2), where n is the maximum of number of rows or columns in the matrix A.
#
# tC: The time complexity of the solution is O(n^2),
# where n is the maximum of number of rows or columns in the matrix A.
# Therefore, the time complexity of the solution is quadratic in terms of input size,
# which is considered to be moderately efficient.
