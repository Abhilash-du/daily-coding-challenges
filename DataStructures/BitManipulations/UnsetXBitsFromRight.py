# Given an integer A. Unset B bits from the right of A in binary.
# For eg:-
# A = 93, B = 4
# A in binary = 1011101
# A should become = 1010000 = 80. Therefore return 80.
#
#
# Problem Constraints
# 1 <= A <= 1018
# 1 <= B <= 60
#
#
# Input Format
# The first argument is a single integer A.
# The second argument is a single integer B.
#
#
# Output Format
# Return the number with B unset bits from the right.
#
#
# Example Input
# Input 1:-
# A = 25
# B = 3
# Input 2:-
# A = 37
# B = 3
#
#
# Example Output
# Output 1:-
# 24
# Output 2:-
# 32
#
#
# Example Explanation
# Explanation 1:-
# A = 11001 to 11000
# Explantion 2:-
# A = 100101 to 100000

class Solution:
    # @param A : long
    # @param B : integer
    # @return an long
    def solve(self, A, B):
        return (A >> B) << B

# Approach Followed:-
#  Since we have to Unset B bits from the right of A in binary,
#  which means the bits in the left side of Bth index(from right) needs to be unchanged and the right side will be unset
# So we can first remove the last B bits by doing right shift (ex: A:1010011, B:4 --> A>>B: 101)
# Now after removing the bits we have to add B unset bits to the right of the array A
# To achieve this we can now use left shift which will add unset bits to the right of array and this will be final value
# Example:-
# A=1010011, B=4
#  A>>B (1010011>>4)--> 101
#  A<<B (101<<4)--> 1010000  (Final Value)
