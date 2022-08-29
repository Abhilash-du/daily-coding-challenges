# Problem Description
# Given an array of integers A, a subarray of an array is said to be good if it fulfills any one of the criteria:
# 1. Length of the subarray is be even, and the sum of all the elements of the subarray must be less than B.
# 2. Length of the subarray is be odd, and the sum of all the elements of the subarray must be greater than B.
# Your task is to find the count of good subarrays in A.
#
# Problem Constraints
# 1 <= len(A) <= 103
# 1 <= A[i] <= 103
# 1 <= B <= 107
#
# Input Format
# The first argument given is the integer array A.
# The second argument given is an integer B.
#
# Output Format
# Return the count of good subarrays in A.
#
# Example Input
# Input 1:
# A = [1, 2, 3, 4, 5]
# B = 4
# Input 2:
#
# A = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
# B = 65
#
#
# Example Output
# Output 1:
# 6
# Output 2:
#
# 36
#
#
# Example Explanation
# Explanation 1:
# Even length good subarrays = {1, 2}
# Odd length good subarrays = {1, 2, 3}, {1, 2, 3, 4, 5}, {2, 3, 4}, {3, 4, 5}, {5}

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        count = 0
        for i in range(n):
            sub_len = 0  # length counter
            sub_sum = 0
            for j in range(i, n):
                sub_len += 1
                sub_sum += A[j]  # sum calculation
                if sub_len % 2 == 0 and sub_sum < B:  # for even good sub-array
                    count += 1
                if sub_len % 2 == 1 and sub_sum > B:  # for odd good sub-array
                    count += 1
        return count

# Approach followed/Observation:-
# Since the constraints are small we can generate all sub-arrays using 2 loops. This can be done in O(N^2).
# Then find the sum of each sub-array and check both the conditions.
# Note that we cannot iterate over the sub-array after generating the left index and right index to find the sum as
# this will increase the time complexity of the solution to O(N^3). We can find the sum of each sub-array in O(1) with
# the help of a prefix sum array, which takes an O(N) pre-computation.
