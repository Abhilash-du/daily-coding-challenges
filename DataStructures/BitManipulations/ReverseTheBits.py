# Problem Description
# Reverse the bits of an 32 bit unsigned integer A.
#
# Problem Constraints
# 0 <= A <= 232
#
# Input Format
# First and only argument of input contains an integer A.
#
# Output Format
# Return a single unsigned integer denoting the decimal value of reversed bits.
#
# Example Input
# Input 1:  0
# Input 2:  3
#
# Example Output
# Output 1:  0
# Output 2:  3221225472
#
# Example Explanation
# Explanation 1:
#         00000000000000000000000000000000
# =>      00000000000000000000000000000000
# Explanation 2:
#         00000000000000000000000000000011
# =>      11000000000000000000000000000000
class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        final_val = 0
        for i in range(32):  # total 0 to 31 elements
            n = 31 - i  # for reverse power
            bit_val = A % 2
            final_val += bit_val * (2 ** n)
            A = A >> 1
        return final_val

# Approach followed:-
# We just have to find  the value in reversed manner, so if the bit is one,
# we have to multiply by its reversed index value which can be find using 31-i
# and using that we can find our final value
