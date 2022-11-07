# Problem Description
# Given an even number A ( greater than 2 ), return two prime numbers whose sum will be equal to the given number.
# If there is more than one solution possible, return the lexicographically smaller solution.
# If [a, b] is one solution with a <= b, and [c,d] is another solution with c <= d, then
# [a, b] < [c, d], If a < c OR a==c AND b < d.
# NOTE: A solution will always exist. Read Goldbach's conjecture.
#
# Problem Constraints
# 4 <= A <= 2*107
#
# Input Format
# First and only argument of input is an even number A.
#
# Output Format
# Return a integer array of size 2 containing primes whose sum will be equal to given number.
#
# Example Input
#  4
#
# Example Output
#  [2, 2]
#
# Example Explanation
#  There is only 1 solution for A = 4.

class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        for i in range(2, A):
            num1 = i
            num2 = A - i
            if self.checkPrime(num1) and self.checkPrime(num2):
                return [num1, num2]
        return []

    def checkPrime(self, A):
        num = 2
        while num * num <= A:
            if A % num == 0:
                return False
            num += 1
        return True


