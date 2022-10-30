# Problem Description
# Given an array A of N integers.
# Find the largest continuous sequence in a array which sums to zero.
#
# Problem Constraints
# 1 <= N <= 106
# -107 <= A[i] <= 107
#
# Input Format
# Single argument which is an integer array A.
#
# Output Format
# Return an array denoting the longest continuous sequence with total sum of zero.
# NOTE : If there are multiple correct answers, return the sequence which occurs first in the array.
#
# Example Input
# A = [1,2,-2,4,-4]
#
# Example Output
# [2,-2,4,-4]
#
# Example Explanation
# [2,-2,4,-4] is the longest sequence with total sum of zero.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        A = [0] + A

        n = len(A)
        hmap = {}

        preSum = 0
        start = 0
        end = 0
        max_len = -1

        for i in range(n):
            preSum += A[i]
            if preSum in hmap:
                seq = i - hmap[preSum]
                if seq > max_len:
                    max_len = seq
                    start = hmap[preSum]
                    end = i
            else:
                hmap[preSum] = i
        return A[start + 1:end + 1]

# Observation/Approach Followed:-
# Loop through each element in the array and keep summing up the values, if sum-value is repeated means the sum till
# i is zero. Since we have to find the max continuous sequence we will just be storing the first index found
# we can find the length by end-start and compare the max length each time
