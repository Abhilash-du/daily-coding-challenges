# Problem Description
# Write a function that takes an integer and returns the number of 1 bits it has.
#
# Problem Constraints
# 1 <= A <= 109
#
# Input Format
# First and only argument contains integer A
#
# Output Format: Return an integer as the answer
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
        i = A
        count = 0
        while i > 0:
            if i % 2 == 1:  # remainder as 1
                count += 1
            i = i >> 1
        return count
