# Problem Description
# Given an integer A, find and return the Ath magic number.
#
# A magic number is defined as a number that can be expressed as a power of 5 or a sum of unique powers of 5.
#
# First few magic numbers are 5, 25, 30(5 + 25), 125, 130(125 + 5), ….
#
# Problem Constraints
# 1 <= A <= 5000
#
# Input Format
# The only argument given is integer A.
#
# Output Format
# Return the Ath magic number.
#
# Example Input
# Example Input 1: A = 3
# Example Input 2: A = 10
#
# Example Output
# Example Output 1:  30
# Example Output 2:  650
#
# Example Explanation
# Explanation 1: Magic Numbers in increasing order are [5, 25, 30, 125, 130, ...]
#  3rd element in this is 30
# Explanation 2:  In the sequence shown in explanation 1, 10th element will be 650.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        ans = 0
        power = 1
        while A > 0:
            if A & 1:
                ans += (5 ** power)
            A = A >> 1
            power += 1
        return ans

# Observation/Approach Followed:-
# As we know **5n > 51 + 52 + ... + 5n-1**
# So, we can find the sum of all subsets of the first 13 power of 5.
# since no element will overlap, we will have 2^13 - 1 elements or 8000 elements.
# Simply sort them and answer the query in O(1).
# Time Complexity: O(A*logA).
#
# Else we can use a much faster approach.
# We can represent A in its binary representation.
# If the ith bit(1 based indexing) is set we will add 5i to our answer.
# Time Complexity:- O(log(A))
