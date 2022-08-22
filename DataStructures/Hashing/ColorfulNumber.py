# Problem Description
# Given a number A, find if it is COLORFUL number or not.
# If number A is a COLORFUL number return 1 else, return 0.
#
# What is a COLORFUL Number:
# A number can be broken into different contiguous sub-subsequence parts.
# Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
# And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different.
#
# Problem Constraints
# 1 <= A <= 2 * 109
#
# Input Format
# The first and only argument is an integer A.
#
# Output Format
# Return 1 if integer A is COLORFUL else return 0.
#
# Example Input
# Input 1:  A = 23
# Input 2:  A = 236
#
# Example Output
# Output 1:  1
# Output 2:  0
#
# Example Explanation:-
#
# Explanation 1:
#  Possible Sub-sequences: [2, 3, 23] where
#  2 -> 2
#  3 -> 3
#  23 -> 6  (product of digits)
#  This number is a COLORFUL number since product of every digit of a sub-sequence are different.
#
# Explanation 2:
#  Possible Sub-sequences: [2, 3, 6, 23, 36, 236] where
#  2 -> 2
#  3 -> 3
#  6 -> 6
#  23 -> 6  (product of digits)
#  36 -> 18  (product of digits)
#  236 -> 36  (product of digits)
#  This number is not a COLORFUL number since the product sequence 23  and sequence 6 is same.
class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        str_A = str(A)
        n = len(str_A)
        set_val = set()
        for i in range(n):
            prod = 1
            for j in range(i, n):
                prod = prod * int(str_A[j])
                if prod in set_val:
                    return 0
                else:
                    set_val.add(prod)
        return 1

# Explanation/Observation:-
# You just need to simulate what has been stated in the problem.
# Iterate over all substrings of number, and then check if the number resulting from the multiplication has
# been stored by us or not using hashing.
