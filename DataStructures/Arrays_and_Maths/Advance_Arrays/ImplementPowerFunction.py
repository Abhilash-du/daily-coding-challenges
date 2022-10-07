# Problem Description
# Implement pow(A, B) % C.
# In other words, given A, B and C, Find (AB % C).
#
# Note: The remainders on division cannot be negative. In other words, make sure the answer you return is non-negative.
#
# Problem Constraints
# -109 <= A <= 109
# 0 <= B <= 109
# 1 <= C <= 109
#
# Input Format
# Given three integers A, B, C.
#
# Output Format
# Return an integer.
#
# Example Input
# A = 2, B = 3, C = 3
#
# Example Output
# 2
#
# Example Explanation
# 23 % 3 = 8 % 3 = 2


class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if A == 0 and B == 0 or A == 0:
            return 0
        if B == 0:
            return 1
        val = pow(A, B // 2, C)  # recursive check

        if B % 2 == 0:
            return (val % C * val % C) % C  # in case of even power value
        else:
            return (val % C * val % C * A % C) % C  # in case of odd power value
