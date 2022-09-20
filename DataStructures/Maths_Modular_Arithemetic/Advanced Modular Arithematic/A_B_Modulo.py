# Q2. A, B and Modulo
# Problem Description
# Given two integers A and B, find the greatest possible positive integer M, such that A % M = B % M.
#
# Problem Constraints
# 1 <= A, B <= 109
# A != B
#
# Input Format
# The first argument is an integer A.
# The second argument is an integer B.
#
# Output Format
# Return an integer denoting the greatest possible positive M.
#
# Example Input
# Input 1:
# A = 1
# B = 2
# Input 2:
# A = 5
# B = 10
#
# Example Output
# Output 1: 1
# Output 2: 5
#
# Example Explanation
# Explanation 1: 1 is the largest value of M such that A % M == B % M.
# Explanation 2: For M = 5, A % M = 0 and B % M = 0.
#
# No value greater than M = 5, satisfies the condition.

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        return abs(A-B)

# Observation/Approach Followed:-
# We can find the value of M by looping from 1 to min(A, B) and storing the maximum M,
# which satisfies the equation A%M == B%M.
#
# But this approach will take time complexity of O(min(A, B)). So that will not work.
#
# As provided in the problem that we have to find the greatest possible positive integer M, such that "A % M = B % M"
# So,
# A%M = B%M
# above can be written as : A%M - B%M =0
# Now as we can take common: (A - B)%M=0
# This can further considered as: A%M - B%M +M%M =0
#  M%M will be zero so: A%M - B%M=0
#  SO finally we can say: (A-B)%M = 0 --> proved
#  Basically M=A-B, where A>B
# Where A-B will be the greatest value M value
