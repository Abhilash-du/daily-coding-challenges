# Problem Description:-
#
# Given an array of integers A and an integer B. You must modify the array exactly B number of
# times. In a single modification, we can replace any one array element A[i] by -A[i].
#
# You need to perform these modifications in such a way that after exactly B modifications, sum of the array must be
# maximum.
#
# Problem Constraints
# 1 <= length of the array <= 5*105
# 1 <= B <= 5 * 106
# -100 <= A[i] <= 100
#
# Input Format
# The first argument given is an integer array A.
# The second argument given is an integer B.
#
# Output Format
# Return an integer denoting the maximum array sum after B modifications.
#
# Example Input
# Input 1:
#  A = [24, -68, -29, -9, 84]
#  B = 4
# Input 2:
#  A = [57, 3, -14, -87, 42, 38, 31, -7, -28, -61]
#  B = 10
#
# Example Output
# Output 1:  196
# Output 2:  362
#
# Example Explanation
# Explanation 1:  Final array after B modifications = [24, 68, 29, -9, 84]
# Explanation 2:  Final array after B modifications = [57, -3, 14, 87, 42, 38, 31, 7, 28, 61]

import heapq


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        heapq.heapify(A)
        while B > 0:
            # pop minimum element from the queue
            val = -1 * heapq.heappop(A)
            heapq.heappush(A, val)
            B -= 1
        ans = 0
        for val in A:
            # add all the elements in the queue
            ans += val
        return ans

# Solution Approach:-
# This problem can simply be solved by just changing the minimum element A[i] to -A[i].
# Keep on getting the minimum element from the array and multiply that element by -1. Do this exactly B times.
# It is easy to observe that if the minimum element is zero, we can’t increase our answer by any modification.
# Time Complexity: B log N
