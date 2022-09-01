# Problem Description
# You are given a 2D integer matrix A, make all the elements in a row or
# column zero if the A[i][j] = 0. Specifically, make entire ith row and jth column zero.
#
# Problem Constraints
# 1 <= A.size() <= 103
# 1 <= A[i].size() <= 103
# 0 <= A[i][j] <= 103
#
# Input Format
# First argument is a vector of vector of integers.(2D matrix).
#
# Output Format
# Return a vector of vector after doing required operations.
#
# Example Input
# Input 1:
# [1,2,3,4]
# [5,6,7,0]
# [9,2,0,4]
#
# Example Output
# Output 1:
# [1,2,0,0]
# [0,0,0,0]
# [0,0,0,0]
#
# Example Explanation
# Explanation 1:
# A[2][4] = A[3][3] = 0, so make 2nd row, 3rd row, 3rd column and 4th column zero.

class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def solve(self, A):
        n1 = len(A)
        column_list = []
        for i in range(n1):
            zero_flag = False  # flag to check zero already present
            n2 = len(A[0])
            for j in range(n2):
                if A[i][j] == 0:
                    zero_flag = True
                    column_list.append(j)  # append column numbers that needs to be updated
            if zero_flag:
                A[i] = [0] * n2  # Making all columns zero

        for i in range(n1):
            for item in column_list:
                A[i][item] = 0
        return A

# Approach Followed:-
# We will first find out the rows in which items are already zero, and we will
# replace whole row by zero
# Also we will keep track of the column number in which the zeroes were found
# So at the final loop we will be moving through each row of Array and will only replace
# zero to specific columns from column number list present
