# Problem Description
# Write a function that takes an integer and returns the number of 1 bits it has.
#
# Problem Constraints
# 1 <= A <= 109
#
# Input Format
# First and only argument contains integer A
#
# Output Format
# Return an integer as the answer
#
# Example Input
# Input1: 11
#
# Example Output
# Output1: 3
#
# Example Explanation
# Explanation1: 11 is represented as 1011 in binary.

class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        while A > 0:
            if A & 1 == 1:  # checking LSB
                count += 1
            A = A >> 1  # dividing by 2 using right shift
        return count

# Observation/Approach Followed:-
# This special solution uses a trick which is normally used in bit manipulations.
# Notice what x - 1 does to bit representation of x.
# x - 1 would find the first set bit from the end, and then set it to 0, and set all the bits following it.
#
# Which means if x = 10101001010100
#                               ^
#                               |
#                               |
#                               |
#
#                        First set bit from the end
# Then x - 1 becomes 10101001010(011)
#
# All other bits in x - 1 remain unaffected. This means that if we do (x & (x - 1)), it would just unset the last set
# bit in x (which is why x&(x-1) is 0 for powers of 2).
#
# Can you use the above fact to come up with a solution ?
