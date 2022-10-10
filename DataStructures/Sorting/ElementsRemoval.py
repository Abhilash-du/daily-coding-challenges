# Problem Description
# Given an integer array A of size N. You can remove any element from the array in one operation.
# The cost of this operation is the sum of all elements in the array present before this operation.
#
# Find the minimum cost to remove all elements from the array.
#
# Problem Constraints
# 0 <= N <= 1000
# 1 <= A[i] <= 103
#
# Input Format
# First and only argument is an integer array A.
#
# Output Format
# Return an integer denoting the total cost of removing all elements from the array.
#
# Example Input
# Input 1:  A = [2, 1]
# Input 2:  A = [5]
#
#
# Example Output
# Output 1:
#
#  4
# Output 2:
#
#  5
#
#
# Example Explanation
# Explanation 1:
#
#  Given array A = [2, 1]
#  Remove 2 from the array => [1]. Cost of this operation is (2 + 1) = 3.
#  Remove 1 from the array => []. Cost of this operation is (1) = 1.
#  So, total cost is = 3 + 1 = 4.
# Explanation 2:
#
#  There is only one element in the array. So, cost of removing is 5.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        n = len(A)
        sum = 0
        for i in range(n):
            sum += A[i] * (n - i)
        return sum

# Approach Followed/Observation:-
#
# Let’s find the count of how many times an element will contribute to the answer.
#
# Remove any element from the array. The cost of this operation is equal to the sum of array elements irrespective of
# which element gets removed.
#
# If we remove another element from the array, the cost of this operation will be ( cost of the previous operation -
# the element which gets removed in the last operation.)
#
# So, we can easily observe that it is wise to remove the highest element first to make the total cost minimum,
# and elements also follow a pattern.
#
# Element removed first will be added 1 time to the answer.
# Element removed second will be added 2 times to the answer.
# Element removed third will be added 3 times to the answer.
# .
# .
# .
# So on.
#
# We can easily find the total cost in one single loop.
