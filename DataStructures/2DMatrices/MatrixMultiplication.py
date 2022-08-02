# Problem Description
# You are given two integer matrices A(having M X N size) and B(having N X P).
# You have to multiply matrix A with B and return the resultant matrix. (i.e. return the matrix AB).
#
# Problem Constraints
# 1 <= M, N, P <= 100
# -100 <= A[i][j], B[i][j] <= 100
#
# Input Format
# First argument is a 2D integer matrix A.
# Second argument is a 2D integer matrix B.
#
# Output Format
# Return a 2D integer matrix denoting AB.
#
# Example Input
# Input 1:
#  A = [[1, 2],            B = [[5, 6],
#       [3, 4]]                 [7, 8]]
# Input 2:
#  A = [[1, 1]]            B = [[2],
#                               [3]]
# Example Output
# Output 1:
#  [[19, 22],
#   [43, 50]]
# Output 2:
#  [[5]]

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        row_a = len(A)
        row_b = len(B)
        col_b = len(B[0])
        # matrix(i*j) * matrix(j*k)= matrix(i*k)
        mult_matrix = [[0 for _ in range(col_b)] for _ in range(row_a)]
        for i in range(row_a):
            for j in range(col_b):
                for k in range(row_b):
                    product = A[i][k] * B[k][j]
                    mult_matrix[i][j] = mult_matrix[i][j] + product
        return mult_matrix


#To execute the method:-
matrix_multiply = Solution()
A = [
    [1, 2],
     [3, 4]
]
B = [
        [5, 7],
        [8, 9]
]
print(matrix_multiply.solve(A,B))


#Observation and Appproach followed:-
# If two matrices A (M x N) and B (N x P) are multiplied,
# then the order of the resultant matrix C will be (M x P).
#
# Algorithm
# Define C matrix as (M x P) having initial values equal to 0.
# for i in range 0 to M - 1, do
# for j in range 0 to N – 1, do
# for k in range 0 to P - 1, do
# C[i, j] = C[i, j] + (A[i, k] * B[k, j])