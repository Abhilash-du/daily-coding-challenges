# Problem Description
# Given a string A, you are asked to reverse the string and return the reversed string.
#
# Problem Constraints
# 1 <= |A| <= 105
# String A consist only of lowercase characters.
#
# Input Format
# First and only argument is a string A.
#
# Output Format
# Return a string denoting the reversed string.
#
# Example Input
# Input 1:  A = "scaler"
# Input 2:  A = "academy"
#
# Example Output
# Output 1:  "relacs"
# Output 2:  "ymedaca"
#
# Example Explanation
# Explanation 1:  Reverse the given string.

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        A = list(A)
        for i in range(n // 2):
            A[i], A[n - i - 1] = A[n - i - 1], A[i]
        return "".join(A)

# Approaches considered:-
# One idea is to create new string, iterate A in reverse order
# store each character in the new string.
#
# Other is to do implace reverse operation on the string.
# This can be done, by iterating the first half of the string,
# let's say we are at index i then,
# swap(A[i], A[n-i-1])
# where n is the length of string.
