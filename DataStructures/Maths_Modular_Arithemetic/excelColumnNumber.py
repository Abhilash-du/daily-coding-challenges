# Problem Description
# Given a column title as appears in an Excel sheet, return its corresponding column number.
#
# Problem Constraints
# 1 <= length of the column title <= 5
#
# Input Format
# The only argument is a string that represents the column title in the excel sheet.
#
# Output Format
# Return a single integer that represents the corresponding column number.
#
# Example Input
# Input 1:  AB
# Input 2:  BB
#
# Example Output
# Output 1:  28
# Output 2:  54
#
# Example Explanation
# Explanation 1:
#  A -> 1
#  B -> 2
#  C -> 3
#  ...
#  Z -> 26
#  AA -> 27
#  AB -> 28
# Explanation 2:
#
#  A -> 1
#  B -> 2
#  C -> 3
#  ...
#  Z -> 26
#  AA -> 27
#  AB -> 28
#  ...
#  AZ -> 52
#  BA -> 53
#  BB -> 54

class Solution:
    def titleToNumber(self, A):
        A = A[::-1]
        n = len(A)
        final_val = 0
        for i in range(n):
            k = 26 ** i
            item = ord(A[i]) - 64  # changing order of character, starts with 1 for A
            final_val += k * item
        return final_val

# Observation/Approach Followed:-
# Simple math.
# This is just like base 26 number conversion.
# number = 26^0 * (S[n - 1] - ‘A’ + 1) + 26^1 * (S[n - 2] - ‘A’ + 1) + ….
