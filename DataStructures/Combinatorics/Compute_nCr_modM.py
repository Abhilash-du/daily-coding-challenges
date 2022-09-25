# Q1. Compute nCr % m
#
# Problem Description :-
# Given three integers A, B, and C, where A represents n,
# B represents r, and C represents m, find and return the value of nCr % m where nCr % m = (n!/((n-r)!*r!))% m.
# x! means factorial of x i.e. x! = 1 * 2 * 3... * x.
#
# Problem Constraints
# 1 <= A * B <= 106
# 1 <= B <= A
# 1 <= C <= 106
#
# Input Format
# The first argument given is integer A ( = n).
# The second argument given is integer B ( = r).
# The third argument given is integer C ( = m).
#
# Output Format
# Return the value of nCr % m.
#
# Example Input
# Input 1:
#  A = 5
#  B = 2
#  C = 13
#
# Input 2:
#  A = 6
#  B = 2
#  C = 13
#
# Example Output
# Output 1:10
# Output 2: 2
#
#
# Example Explanation
# Explanation 1:  The value of 5C2 % 11 is 10.
# Explanation 2:  The value of 6C2 % 13 is 2.

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        max_val = max(A, B)
        denom = 1  # to store denominator
        num = 1  # to store numerator
        for i in range(0, B):
            num *= (max_val - i)

        for j in range(1, B + 1):
            denom *= j

        final_val = num // denom
        return final_val % C

# Approach Followed:-
# Since we know nCr = n!/((n-r)!*r!.
# So from above formula lets check an example:-
# 10C2 --> (10*9*8!)/8!*2! , which can further be written as: (10*9)/2!  [8! is removed]
#
#  so NUMERATOR will be 10*9*8, we can check for numerator we just have to multiply first B elements by decrementing
#  Basically numerator can be like: n*(n-1)*(n-2)..*(n-B+1)
#
# Denominator will be just 2!, (or B)
#
# So based on above observation we will first have to find numerator by multiplying till n*n-1..*n-B
# and denominator as: B!
# Final answer will have to return (numerator/denominator)%B
