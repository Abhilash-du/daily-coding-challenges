# Problem Description
# Given a number A, check if it is a magic number or not.
#
# A number is said to be a magic number if the sum of its digits is calculated till a single digit recursively
# by adding the sum of the digits after every addition. If the single digit comes out to be 1,
# then the number is a magic number.
#
# Problem Constraints
# 1 <= A <= 109
#
# Input Format: The first and only argument is an integer A.
#
# Output Format: Return an 1 if the given number is magic else return 0.
#
# Example Input
# Input 1:  A = 83557
# Input 2:  A = 1291
#
# Example Output
# Output 1:  1
# Output 2:  0
#
# Example Explanation
# Explanation 1:
#  Sum of digits of (83557) = 28
#  Sum of digits of (28) = 10
#  Sum of digits of (10) = 1.
#  Single digit is 1, so it's a magic number. Return 1.
#
# Explanation 2:
#  Sum of digits of (1291) = 13
#  Sum of digits of (13) = 4
#  Single digit is not 1, so it's not a magic number. Return 0.

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        return isMagic(A)


def isMagic(num):
    num = check_sum(num)
    if num == 1:  # if sum of digits is one
        return 1
    if num // 10 == 0:  # if single digit number is zero
        return 0
    return isMagic(num)


def check_sum(num):
    if num == 0:
        return 0
    return num % 10 + check_sum(num // 10)

# Recursive Approach:-
# One approach is to recursively check the sum of digits until a single digit is left.
# Now, check if the number is 1, then it is a magic number. Else NOT.
#
# Efficient Approach:
# There is also a shortcut method to verify Magic Number.
# The function will determine if the remainder of dividing the input by 9 is 1 or not.
# If it is 1, then the number is a magic number.
# The divisibility rule of 9 says that a number is divisible by 9 if the sum of its digits is also divisible by 9.
# Therefore, if a number is divisible by 9, then, recursively, all the digit sums are also divisible by 9.
# The final digit sum is always 9. An increase of 1 in the original number will increase the ultimate value by 1,
# making it 10, and the ultimate sum will be 1, thus verifying that it is a magic number.