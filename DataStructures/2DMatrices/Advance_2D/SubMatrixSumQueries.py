# Problem Description
# Given a matrix of integers A of size N x M and multiple queries Q, for each query, find and return the submatrix sum.
#
# Inputs to queries are top left (b, c) and bottom right (d, e) indexes of submatrix whose sum is to find out.
#
# NOTE:
#
# Rows are numbered from top to bottom, and columns are numbered from left to right.
# Sum may be large, so return the answer mod 109 + 7.
#
#
# Problem Constraints
# 1 <= N, M <= 1000
# -100000 <= A[i] <= 100000
# 1 <= Q <= 100000
# 1 <= B[i] <= D[i] <= N
# 1 <= C[i] <= E[i] <= M
#
#
#
# Input Format
# The first argument given is the integer matrix A.
# The second argument given is the integer array B.
# The third argument given is the integer array C.
# The fourth argument given is the integer array D.
# The fifth argument given is the integer array E.
# (B[i], C[i]) represents the top left corner of the i'th query.
# (D[i], E[i]) represents the bottom right corner of the i'th query.
#
#
#
# Output Format
# Return an integer array containing the sub-matrix sum for each query.
#
# Example:-
# Input 1:
#
#  A = [   [1, 2, 3]
#          [4, 5, 6]
#          [7, 8, 9]   ]
#  B = [1, 2]
#  C = [1, 2]
#  D = [2, 3]
#  E = [2, 3]

# Input 2:
#
#  A = [   [5, 17, 100, 11]
#          [0, 0,  2,   8]    ]
#  B = [1, 1]
#  C = [1, 4]
#  D = [2, 2]
#  E = [2, 4]
#
# Example Output
# Output 1:  [12, 28]
# Output 2:  [22, 19]
# Example Explanation
# Explanation 1:
#  For query 1: Sub-matrix contains elements: 1, 2, 4 and 5. So, their sum is 12.
#  For query 2: Sub-matrix contains elements: 5, 6, 8 and 9. So, their sum is 28.
#
# Explanation 2:
#  For query 1: Sub-matrix contains elements: 5, 17, 0 and 0. So, their sum is 22.
#  For query 2: Sub-matrix contains elements: 11 and 8. So, their sum is 19.
class Solution:
    # @param A : list of list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @param D : list of integers
    # @param E : list of integers
    # @return a list of integers
    def solve(self, A, B, C, D, E):
        n = len(A)
        m = len(A[0])
        newA = [[0 for _ in range(m + 1)] for __ in range(n + 1)]  # Adding extra zero row and column1
        for row in range(1, n + 1):
            for column in range(1, m + 1):  # Creating prefix sum matrix
                newA[row][column] = A[row - 1][column - 1] + newA[row - 1][column] + newA[row][column - 1] - \
                                    newA[row - 1][column - 1]

        final_arr = []
        for idx in range(len(B)):
            i, k = B[idx], D[idx]  # i,j-->starting index , k,l --> end index
            j, l = C[idx], E[idx]
            final_val = newA[k][l] - newA[k][j - 1] - newA[i - 1][l] + newA[i - 1][j - 1]
            final_arr.append(final_val % (10 ** 9 + 7))

        return final_arr

# Solution Approach:-
# The idea is to first create an auxiliary matrix arr[N+1][M+1] such that arr[i][j] stores sum of elements in
# sub-matrix from (0,0) to (i,j). Once arr[][] is constructed, we can compute sum of sub-matrix between (x1,
# y1) and (x2, y2) in O(1) time. We need to consider arr[x2][y2] and subtract all unnecessary elements. Below is the
# complete expression to compute the sub-matrix sum in O(1) time.
#
# Sum between (x1, y1) and (x2, y2) is,
# arr[x2][y2] - arr[x2][y1-1] - arr[x1-1][y2] + arr[x1-1][y1-1]
#
# The sub-matrix aux[x1-1][x2-1] is added because elements of it are subtracted twice.
# Remember to return the ans%1000000007
