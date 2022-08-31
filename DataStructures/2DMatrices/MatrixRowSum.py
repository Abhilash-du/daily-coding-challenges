# Problem Description
# You are given a 2D integer matrix A, return a 1D integer array containing row-wise sums of original matrix.
#
# Problem Constraints
# 1 <= A.size() <= 103
# 1 <= A[i].size() <= 103
# 1 <= A[i][j] <= 103
#
# Input Format
# First argument A is a 2D array of integers.(2D matrix).
#
# Output Format
# Return an array containing row-wise sums of original matrix.
#
# Example Input
# Input 1:
# [1,2,3,4]
# [5,6,7,8]
# [9,2,3,4]
#
# Example Output
# Output 1: {10,26,18}
#
# Example Explanation
# Explanation 1
# Row 1 = 1+2+3+4 = 10
# Row 2 = 5+6+7+8 = 26
# Row 3 = 9+2+3+4 = 18
class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        n1 = len(A)  # number of rows
        n2 = len(A[0])  # number of columns on each row
        sum_arr = []
        for i in range(n1):
            col_sum = 0
            for j in range(n2):
                col_sum += A[i][j]
            sum_arr.append(col_sum)
        return sum_arr
# Approach Followed:-
# Iterate the 2D vector row wise and by storing sum of a row in a variable and push it in a vector
# after the completion of each row.
