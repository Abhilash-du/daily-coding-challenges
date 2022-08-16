# Problem Description
# On the first row, we write a 0. Now in every subsequent row, we look at the previous row and replace
# each occurrence of 0 with 01, and each occurrence of 1 with 10.
# Given row number A and index B, return the Bth indexed symbol in row A. (The values of B are 1-indexed.).
#
# Problem Constraints
# 1 <= A <= 20
# 1 <= B <= 2A - 1
#
# Input Format
# First argument is an integer A.
# Second argument is an integer B.
#
# Output Format
# Return an integer denoting the Bth indexed symbol in row A.
#
# Example Input
# Input 1:
#  A = 2
#  B = 1
# Input 2:
#  A = 2
#  B = 2
#
# Example Output
# Output 1:  0
# Output 2:  1
#
# Example Explanation
# Explanation 1:
#  Row 1: 0
#  Row 2: 01
#
# Explanation 2:
#  Row 1: 0
#  Row 2: 01

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A == 1:
            return 0
        A_len = 2 ** (A - 1)
        mid = A_len // 2
        if mid >= B:
            return self.solve(A - 1, B)
        else:
            return 1 - self.solve(A - 1, B - mid)  # Swap the element using 1-element(zero or one, depending on element)

# Observation/Approach followed:-
# Each row will be keep increasing by 2 (2^0,2^1,2^3....2^k-1)
# for each nth row number of elements(k) will be n^k-1 (ex: row 2 will have 2^2-1--> 2 elements)
# Each row replicates the same value as its parent row till half elements, after half the value starts to be opposite
# So basically based on the parent element, we can find the new element
# CONDITION1: if the B value from Ath row is less than mid(half of the length) value, then
# we can fetch parent element value at same index
# CONDITION2: if the B value from Ath row is more than mid(half of the length) value, then
# # we can fetch parent element value at index B-mid (basically removing the elements less than mid)
# and then fetch the same value from parent and switch it by using 1-element
# (so that for 1 it will be 0 and 0 it will be 1)
