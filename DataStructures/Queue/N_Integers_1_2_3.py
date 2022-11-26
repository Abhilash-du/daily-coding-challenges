# Problem Description
# Given an integer, A. Find and Return first positive A integers in ascending order containing only digits 1, 2, and 3.
# NOTE: All the A integers will fit in 32-bit integers.
#
# Problem Constraints
# 1 <= A <= 29500
#
# Input Format
# The only argument given is integer A.
#
# Output Format
# Return an integer array denoting the first positive A integers in ascending order containing only digits 1, 2 and 3.
#
# Example Input
# Input 1:  A = 3
# Input 2:  A = 7
#
# Example Output
# Output 1:  [1, 2, 3]
# Output 2:  [1, 2, 3, 11, 12, 13, 21]
#
# Example Explanation
# Explanation 1: Output denotes the first 3 integers that contains only digits 1, 2 and 3.
#
# Explanation 2: Output denotes the first 3 integers that contains only digits 1, 2 and 3.

from collections import deque


class Solution:
    # @param A : integer
    # @return a list of integers
    def solve(self, A):
        queue = deque([1, 2, 3])
        ans = []
        for i in range(A):
            element = queue.popleft()
            ans.append(element)
            for j in range(1, 4):
                # append 1, 2 and 3 to the current number
                queue.append(10 * element + j)
        return ans

# Solution Approach/Observation:-
#
# We know the initial three values will be 1, 2, and 3.
# Now, the upcoming values will be by appending 1, 2, and 3 in each given value.
# We will use a queue to store the elements in ascending order
#
# By default we will keep queue values as 1,2,3
# now for each element we can say 10*element + (1,2,3)
# we will iterate n times and each time we will append rear element of queue in answer
