# Problem Description
# You are given an array of N integers, A1, A2, .... AN.
# Return the maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|,
# where |x| denotes absolute value of x.
#
# Problem Constraints
# 1 <= N <= 100000
# -109 <= A[i] <= 109
#
# Input Format
# First argument is an integer array A of size N.
#
# Output Format
# Return an integer denoting the maximum value of f(i, j).
#
# Example Input
# Input1: A = [1, 3, -1]
# Input2: A = [2]
#
# Example Output
# Output 1: 5
# Output 2: 0

class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArr(self, A):
        max1 = A[0]
        max2 = A[0]
        min1 = A[0]
        min2 = A[0]
        for i in range(len(A)):
            max1 = max(max1, A[i] + i)
            max2 = max(max2, A[i] - i)
            min1 = min(min1, A[i] + i)
            min2 = min(min2, A[i] - i)
        return max(max1 - min1, max2 - min2)

# Approach Followed:-
# f(i, j) = |A[i] - A[j]| + |i - j| can be written in 4 ways (Since we are looking at max value,
# we don’t even care if the value becomes negative as long as we are also covering the max value in some way).
#
# (A[i] + i) - (A[j] + j)
# -(A[i] - i) + (A[j] - j)
# (A[i] - i) - (A[j] - j)
# (-A[i] - i) + (A[j] + j) = -(A[i] + i) + (A[j] + j)
# Note that case 1 and 4 are equivalent and so are case 2 and 3.
#
# We can construct two arrays with values: A[i] + i and A[i] - i. Then, for the above 2 cases,
# we find the maximum value possible. For that, we just have to store minimum and maximum values of expressions
# A[i] + i and A[i] - i for all i.
