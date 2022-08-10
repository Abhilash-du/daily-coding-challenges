# Problem Description
# Write a recursive function that checks whether string A is a palindrome or Not.
# Return 1 if the string A is a palindrome, else return 0.
# Note: A palindrome is a string that's the same when read forward and backward.
#
# Problem Constraints
# 1 <= A <= 50000
# String A consists only of lowercase letters.
#
# Input Format
# The first and only argument is a string A.
#
# Output Format: Return 1 if the string A is a palindrome, else return 0.
#
# Example Input
# Input 1:  A = "naman"
# Input 2:  A = "strings"
#
# Example Output
# Output 1: 1
# Output 2: 0
#
# Example Explanation
# Explanation 1:  "naman" is a palindromic string, so return 1.
# Explanation 2:  "strings" is not a palindrome, so return 0.

import sys

sys.setrecursionlimit(10 ** 6)


def palindrome(A, start, end):
    if start >= end:
        return 1
    if A[start] == A[end]:
        return palindrome(A, start + 1, end - 1)
    return 0


class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        start = 0
        end = len(A) - 1
        return palindrome(A, start, end)

# Solution Approach/ Observation Followed:-
# Consider two indexes i and j, initially at the first and last index of the string, respectively.
# If the character at both i and j index is the same, check recursively for i+1, j-1.
# We can say that, F(i, j) tell if the string from i to j is palindrome or not:
#
# if(A[i] == A[j])
# F(i, j) = F(i+1, j-1)
# else
# F(i, j) = 0
