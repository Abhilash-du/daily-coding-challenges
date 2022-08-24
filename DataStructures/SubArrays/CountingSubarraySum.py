# Problem Description
# Given an array A of N non-negative numbers and a non-negative number B,
# you need to find the number of sub-arrays in A with a sum less than B.
# We may assume that there is no overflow.
#
# Problem Constraints
# 1 <= N <= 103
# 1 <= A[i] <= 1000
# 1 <= B <= 107
#
#
#
# Input Format
# First argument is an integer array A.
# Second argument is an integer B.
#
# Output Format
# Return an integer denoting the number of sub-arrays in A having sum less than B.
#
# Example Input
# Input 1:
#  A = [2, 5, 6]
#  B = 10
# Input 2:
#  A = [1, 11, 2, 3, 15]
#  B = 10
#
# Example Output
# Output 1:  4
# Output 2:  4
#
# Example Explanation
# Explanation 1:  The sub-arrays with sum less than B are {2}, {5}, {6} and {2, 5},
# Explanation 2:  The sub-arrays with sum less than B are {1}, {2}, {3} and {2, 3}


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        total_count = 0
        for i in range(n):
            sub_sum = A[i]  # to store sub array sum
            if sub_sum < B:
                total_count += 1  # increment for single item
            else:
                continue
            for j in range(i + 1, n):
                sub_sum = sub_sum + A[j]
                if sum < B:
                    total_count += 1  # increment count for multiple items
                else:
                    break
        return total_count

# Approach Followed:-
# Since the constraints are small we can generate all sub-arrays using 2 loops.
# This can be done in O(N^2). Then find the sum of each sub-arrays and if the sum is less than B we add 1 to our answer.
