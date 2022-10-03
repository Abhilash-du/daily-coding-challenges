# Q2. Diffk II
# Problem Description
# Given an array A of integers and another non negative integer B .
#
# Find if there exists 2 indices i and j such that A[i] - A[j] = B and i != j.
#
# Problem Constraints
# 1 <= |A| <= 106
# 0 <= A[i] <= 109
# 0 <= B <= 109
#
# Input Format
# First argument A is an array of integer
# Second argument B is an integer
#
# Output Format
# Return 1 if two such indexes are found and 0 otherwise
#
# Example Input
# Input 1:
# A = [1, 5, 3]
# B = 2
#
# Input 2:
# A = [2, 4, 3]
# B = 3
#
# Example Output
# Output 1:
# 1
# Output 2:
# 0
#
# Example Explanation
# For Input 1:
# The given value of A[1] = 1 and A[3] = 3.
# The value of A[3] - A[1] = 2.
# For Input 2:
# There are no pairs such that difference is B.

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        n = len(A)
        hs = {}
        for i in range(n):
            val1 = A[i] - B
            val2 = A[i] + B
            if val1 in hs.keys() or val2 in hs.keys():
                return 1
            hs[A[i]] = i
        return 0

# Solution Approach:-
# We are looking to find pair of integers where A[i] - A[j] = k, k being known entity
# Lets say we fix A[i] ( i.e. we know A[i]), do we know what A[j] should be ?
# A[j] = A[i] - k.
# Also if we fix A[j], how can we find value of A[i]?
# A[i]= k + A[j]
# So basically we have to check that "A[j]+k" and "A[i]-k" are present in the array
# Now to store the value we an use a hashmap/dictionary and validate each time if any of both value is already present
# if present return 1 else return 0
