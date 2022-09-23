# Q2. Concatenate Three Numbers
# Problem Description
# Given three 2-digit integers, A, B, and C, find out the minimum number obtained by concatenating them in any order.
#
# Return the minimum result obtained.
#
#
#
# Problem Constraints
# 10 <= A, B, C <= 99
#
#
#
# Input Format
# The first argument of input contains an integer, A.
#
# The second argument of input contains an integer, B.
#
# The third argument of input contains an integer, C.
#
#
#
# Output Format
# Return an integer representing the answer.
#
#
#
# Example Input
# Input 1:
#
#  A = 10
#  B = 20
#  C = 30
# Input 2:
#
#  A = 55
#  B = 43
#  C = 47
#
#
# Example Output
# Output 1:
#
#  102030
# Output 2:
#
#  434755
#
#
# Example Explanation
# Explanation 1:
#
#  10 + 20 + 30 = 102030
# Explanation 2:
#
#  43 + 47 + 55 = 434755
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        max_val = max(A, B, C)
        min_val = min(A, B, C)
        mid_val = A + B + C - max_val - min_val
        return str(min_val) + str(mid_val) + str(max_val)

# Approach followed/Observation:-
#
# The minimum number will always be formed if the smallest number is taken first,
# the second smallest is taken second, and the largest is taken last.
#
# This will be true only if the numbers have the same length.
#
# So, you can also sort the numbers and concatenate them to get the answer.
