# Problem Description
# Given an array of integers A, find and return whether the given array contains
# a non-empty sub-array with a sum equal to 0.
#
# If the given array contains a sub-array with sum zero return 1, else return 0.
#
# Problem Constraints
# 1 <= |A| <= 100000
# -10^9 <= A[i] <= 10^9
#
# Input Format
# The only argument given is the integer array A.
#
# Output Format
# Return whether the given array contains a sub-array with a sum equal to 0.
#
# Example Input
# Input 1:  A = [1, 2, 3, 4, 5]
# Input 2:  A = [-1, 1]
#
# Example Output
# Output 1:  0
# Output 2:  1
#
# Example Explanation
# Explanation 1:  No subarray has sum 0.
# Explanation 2:  The array has sum 0.
#
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = [0] + A
        hmap = {}
        n = len(A)
        sum = 0
        for i in range(n):
            val = A[i]
            sum += val
            if sum in hmap:
                return 1
            hmap[sum] = i
        return 0
#
# # Approach Followed/Observation:-
# # The idea is to iterate through the array, and for every element A[i],
# # calculate sum of elements from 0 to i (this can simply be done as sum += arr[i]).
# #
# # If the current sum has been seen before, then there is a zero-sum array.
# #
# # Hashing is used to store the sum values so that we can quickly store sum and
# # find out whether the current sum is seen before or not.
