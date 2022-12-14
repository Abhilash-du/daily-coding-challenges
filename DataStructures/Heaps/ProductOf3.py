# Problem Description
# Given an integer array A of size N.
# You have to find the product of the three largest integers in array A from range 1 to i, where i goes from 1 to N.
#
# Return an array B where B[i] is the product of the largest 3 integers in range 1 to i in array A.
# If i < 3, then the integer at index i in B should be -1.
#
# Problem Constraints
# 1 <= N <= 105
# 0 <= A[i] <= 103
#
# Input Format
# First and only argument is an integer array A.
#
# Output Format
# Return an integer array B. B[i] denotes the product of the largest 3 integers in range 1 to i in array A.
#
# Example Input
# Input 1:  A = [1, 2, 3, 4, 5]
# Input 2:  A = [10, 2, 13, 4]
#
# Example Explanation
# Explanation 1:
#  For i = 1, ans = -1
#  For i = 2, ans = -1
#  For i = 3, ans = 1 * 2 * 3 = 6
#  For i = 4, ans = 2 * 3 * 4 = 24
#  For i = 5, ans = 3 * 4 * 5 = 60
#
#  So, the output is [-1, -1, 6, 24, 60].
#
# Explanation 2:
# For i = 1, ans = -1
# For i = 2, ans = -1
# For i = 3, ans = 10 * 2 * 13 = 260
# For i = 4, ans = 10 * 13 * 4 = 520
#
# So, the output is [-1, -1, 260, 520].

import heapq
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        ans = [-1, -1]  # the first two element of the answer will always be -1
        min_heap = []  # min heap to store max 3 values

        product = 1
        for i in range(3):
            # finding out the product of first 3 elements and adding it to min  heap
            product *= A[i]
            min_heap.append(A[i])
        ans.append(product)
        # converting list to heap
        heapq.heapify(min_heap)

        for i in range(3, n):
            if min_heap[0] < A[i]:
                # if the minimum value of min heap is less than the current input value
                heapq.heappop(min_heap)
                # pushing the greater value to the heap
                heapq.heappush(min_heap, A[i])
            product = 1
            for val in min_heap:
                # finding out the product of the elements
                product *= val
            ans.append(product)
        return ans

# Observation/Approach followed:_
# If we have traversed the array till some number (say ith number), we will only add numbers further to it,
# and no deletion will occur.
#
# A min heap will have the smallest number at the top of it. We can iterate over the input list items and validate if
# the minimum number from heap can be replaced with higher number. Each time we will have only 3 higher values in the
# min heap and we will be keep replacing the minimum number from the heap
# #
# Using these observations, we can devise the algorithm to compute the product of the three largest
# numbers from the first number to ith number
