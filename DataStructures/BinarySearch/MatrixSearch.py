# Problem Description:
#
# Given a matrix of integers A of size N x M and an integer B. Write an efficient algorithm that
# searches for integer B in matrix A.
#
# This matrix A has the following properties:
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than or equal to the last integer of the previous row.
# Return 1 if B is present in A, else return 0.
#
# NOTE: Rows are numbered from top to bottom, and columns are from left to right.
#
# Problem Constraints
# 1 <= N, M <= 1000
# 1 <= A[i][j], B <= 106
#
# Input Format
# The first argument given is the integer matrix A.
# The second argument given is the integer B.
#
# Output Format
# Return 1 if B is present in A else, return 0.
#
# Example Input
# Input 1:
# A = [
#       [1,   3,  5,  7]
#       [10, 11, 16, 20]
#       [23, 30, 34, 50]
#     ]
# B = 3
#
# Input 2:
# A = [
#       [5, 17, 100, 111]
#       [119, 120, 127, 131]
#     ]
# B = 3
#
# Example Output
# Output 1: 1
# Output 2: 0
#
# Example Explanation
# Explanation 1:  3 is present in the matrix at A[0][1] position so return 1.
# Explanation 2:  3 is not present in the matrix so return 0.


class Solution:
    # @param A : list of list of integers
    # @param B : integer
    # @return an integer

    # Approach One:- (iterate through each row and perform binary search: BF approach)
    def searchMatrix_BF(self, A, B):
        for arr in A:
            left = 0
            right = len(arr) - 1
            if right <= 0 and arr[right] == B:
                return 1

            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == B:
                    return 1
                elif arr[mid] > B:
                    right = mid - 1
                else:
                    left = mid + 1
        return 0

    # Approach Two:- (instead of considering matrix separate rows, merge all rows and column as one array)
    def searchMatrix_efficient(self, A, B):
        n = len(A)
        m = len(A[0])

        left = 0
        right = (m * n) - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // m  # finding row
            col = mid % m  # finding column

            if A[row][col] == B:
                return 1
            elif A[row][col] > B:
                right = mid - 1
            else:
                left = mid + 1
        return 0

# Observation/ Approach Followed:-
# If you write down the numbers of row 1 followed by numbers in row2, row3, and so on,
# do you think the resulting array would be sorted?
#
# If yes, how do you search for a number efficiently in a sorted array?
#
# Just think of how the index in the array can be translated to the elements in the matrix.
# For eg: Total elements : mn; m = no of rows; n = no of columns.
# Indexing will go from 0 to mn - 1. Since the matrix is sorted, binary search can be applied here.
# We take the mid of the total search space (initially all elements), then translate it to the indexes in the matrix
# by row = int(mid / n) and col = int(mid % n). This is valid because every row contains n elements.
