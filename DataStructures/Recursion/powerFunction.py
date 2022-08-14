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
#
# Output Format
# Return an integer.
#
# Example Input
# A = 2, B = 3, C = 3
#
# Example Output: 2
#
# Example Explanation
# 23 % 3 = 8 % 3 = 2

def powerFun(A, B, C):
    if A == 0:
        return 0
    if B == 0:
        return 1  # any val with power zero is 1
    half = pow(A, B // 2, C)  # storing the half power value
    if B % 2 == 0:
        return (half * half) % C
    else:
        return ((half * half) % C * A % C) % C


# print(powerFun(A=2, B=3, C=3))

# Observation:-
# If number(A) is zero, we cannot find the power of it, so we will return 0
# As we know the power of any number with zero is one, we will return 1
# Now we also know that example: a^4=a^(2+2) => a^2*a^2 (so power of 4 can be subdivided in 2+2)
# We can divide power by 2 recursively until it reaches 0
#  Also in case power is odd, we can understand from below example that we have to multiply extra A in result. Example
# For odd power:  A^5=A^2*A^2*A
# For even power: A^4=A&2*A^2
