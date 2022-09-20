# Q1. Single Number III
# Problem Description
# Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
# Find the two integers that appear only once.
#
# Note: Return the two numbers in ascending order.
#
# Problem Constraints
# 2 <= |A| <= 100000
# 1 <= A[i] <= 109
#
# Input Format
# The first argument is an array of integers of size N.
#
# Output Format
# Return an array of two integers that appear only once.
#
# Example Input
# Input 1:
# A = [1, 2, 3, 1, 2, 4]
#
# Input 2:
# A = [1, 2]
#
#
# Example Output
# Output 1:
# [3, 4]

# Output 2:
# [1, 2]
#
#
# Example Explanation
# Explanation 1: 3 and 4 appear only once.
# Explanation 2: 1 and 2 appear only once.
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A)
        xor = A[0]
        for i in range(1, n):
            xor ^= A[i]
        rsb = xor & ~(xor - 1)  # to find the rightmost set bit
        val1 = 0
        val2 = 0
        for i in range(n):
            # Bitwise & the arr[i] with the sum
            # Two possibilities either result == 0
            # or result > 0
            if rsb & A[i] > 0:
                val1 ^= A[i]
            else:
                val2 ^= A[i]

        val1, val2 = min(val1, val2), max(val1, val2)
        return [val1, val2]

#
# Approach Followed/ Observations:0
# Let x and y be the non-repeating elements we are looking for and arr[] be the input array.
# First, calculate the XOR of all the array elements.
#
#      xor = arr[0]^arr[1]^arr[2].....arr[n-1]
#
# All the bits that are set in xor will be set in one non-repeating element (x or y) and not in others.
# So if we take any set bit of xor and divide the elements of the array in two sets – one set of elements with
# same bit set and another set with same bit not set. By doing so, we will get x in one set and y in another set.
# Now if we do XOR of all the elements in the first set, we will get the first non-repeating element, and by doing
# same in other sets we will get the second non-repeating element.
#
# Let us see an example.
#    arr[] = {2, 4, 7, 9, 2, 4}
# 1) Get the XOR of all the elements.
#      xor = 2^4^7^9^2^4 = 14 (1110)
# 2) Get a number which has only one set bit of the xor.
#    Since we can easily get the rightmost set bit, let us use it.
#      set_bit_no = xor & ~(xor-1) = (1110) & ~(1101) = 0010
#    Now set_bit_no will have only set as rightmost set bit of xor.
# 3) Now divide the elements in two sets and do xor of
#    elements in each set and we get the non-repeating
#    elements 7 and 9. Please see the implementation for this step