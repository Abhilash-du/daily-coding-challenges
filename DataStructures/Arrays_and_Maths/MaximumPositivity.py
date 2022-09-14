# Problem Description
# Given an array of integers A, of size N.
#
# Return the maximum size subarray of A having only non-negative elements. If there are more than one such subarray,
# return the one having the smallest starting index in A.
#
# NOTE: It is guaranteed that an answer always exists.
#
#
#
# Problem Constraints
# 1 <= N <= 105
#
# -109 <= A[i] <= 109
#
#
#
# Input Format
# The first and only argument given is the integer array A.
#
#
#
# Output Format Return maximum size subarray of A having only non-negative elements. If there are more than one such
# subarrays, return the one having earliest starting index in A.
#
#
#
# Example Input
# Input 1:
#
#  A = [5, 6, -1, 7, 8]
# Input 2:
#
#  A = [1, 2, 3, 4, 5, 6]
#
#
# Example Output
# Output 1:
#
#  [5, 6]
# Output 2:
#
#  [1, 2, 3, 4, 5, 6]
#
#
# Example Explanation
# Explanation 1:
#
#  There are two sub-arrays of size 2 having only non-negative elements.
#  1. [5, 6]  starting point  = 0
#  2. [7, 8]  starting point  = 3
#  As starting point of 1 is smaller, return [5, 6]
# Explanation 2:
#
#  There is only one sub-array of size 6 having only non-negative elements:
#  [1, 2, 3, 4, 5, 6]
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        s = 0
        e = 0
        s_index = 0  # for temporarily storing start index
        max_len = -1  # to check on maximum length
        for i in range(n):
            element = A[i]
            if element < 0:
                s_index = i + 1
            if element >= 0 and s_index <= i:
                temp_len = i - s_index + 1
                if max_len < temp_len:
                    max_len = temp_len
                    s = s_index  # storing final start and end
                    e = i
        return A[s:e + 1]

# Approach Followed:-
#
# For all elements in array :-
#
# 1.If ith element is negative, we need to ignore it and go on next element
#
# 2. If ith element is non-negative, we will start a second while loop from this position until a negative element
# arrives. a.If size of subarray received using this is greater than size of previous such arrays, then update the
# answer b. else ignore it.
