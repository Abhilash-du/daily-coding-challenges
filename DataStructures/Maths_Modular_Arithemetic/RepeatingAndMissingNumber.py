# Q1. Repeat and Missing Number Array Solved character background character Stuck somewhere? Ask for help from a TA
# and get it resolved. Get help from TA. There are certain problems which are asked in the interview to also check
# how you take care of overflows in your problem. This is one of those problems. Please take extra care to make sure
# that you are type-casting your ints to long properly and at all places. Try to verify if your solution works if
# number of elements is as large as 105
#
# Food for thought :
#
# Even though it might not be required in this problem, in some cases, you might be required to order the operations
# cleverly so that the numbers do not overflow. For example, if you need to calculate n! / k! where n! is factorial(
# n), one approach is to calculate factorial(n), factorial(k) and then divide them. Another approach is to only
# multiple numbers from k + 1 ... n to calculate the result. Obviously approach 1 is more susceptible to overflows.
# You are given a read only array of n integers from 1 to n.
#
# Each integer appears exactly once except A which appears twice and B which is missing.
#
# Return A and B.
#
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Note that in your output A should precede B.
#
# Example:
#
# Input:[3 1 2 5 3]
#
# Output:[3, 4]
#
# A = 3, B = 4

class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        n = len(A)
        expected_sum = n * (n + 1) // 2  # a+b+c+d  (Actual sum from 1+2+...+N)
        expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6  # sq.a+sq.b+sq.c+sq.d, Sum after squaring 1 to N

        actual_sum = 0
        actual_sq_sum = 0

        for i in range(n):
            actual_sum += A[i]  # a+b+c+c
            actual_sq_sum += A[i] ** 2  # sq.a+sq.b+sq.c+sq.c

        sum_diff = expected_sum - actual_sum  # d-c
        sum_sq_diff = expected_sq_sum - actual_sq_sum  # sq.d-sq.c

        duplicate = ((sum_sq_diff // sum_diff) + sum_diff) // 2  # d
        missing = sum_diff - duplicate  # c

        return [abs(missing), abs(duplicate)]

# Approach Followed:-
# As mentioned in the problem we have to find the value without using extra space
# So lets derive it by using below example, where c is repeating character and d is missing
#
# Equation1: (a+b+c+d) - (a+b+c+c) --> d-c,
# now from above equation lets say, k1=d-c
#
# Equation2: (sq(a)+sq(b)+sq(c)+sq(d)) - (sq(a)+sq(b)+sq(c)+sq(c)) --> sq(d)-sq(c)
# now from above equation lets say, k2=sq(d)-sq(c)
#
# Equation 3: now by dividing k2 by k1 we can say: k2/k1= d+c
# Now from above equation lets say, k3=d+c
#
# Now inorder to find the c , we can subtract k3 with k1
#  k3-k1== d+c-d+c (lets take k3-k1 as constant c1)
#   c1=2c
#  c= c1//2  --> using this we can get value of c
#
# Similarly,to find value of d, we can subtract c with k1
#  k1-c== d-c+c --> d
#
#  NOw we have both c and d with us, which are duplicate value and missing value
# Time complexity for this algorithm will be O(N) and Space Complexity will be O(1)
