# Problem Description
# Write a program to find the factorial of the given number A.
#
# Problem Constraints: 0 <= A <= 12
#
# Input Format: First and only argument is an integer A.
#
# Output Format: Return an integer denoting the factorial of the number A.
#
# Example Input
# Input 1:  A = 4
# Input 2:  A = 1
#
# Example Output
# Output 1:  24
# Output 2:  1
#
# Example Explanation
# Explanation 1:  Factorial of 4 = 4 * 3 * 2 * 1 = 24
# Explanation 2:  Factorial of 1 = 1
class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if A == 1:  # N factorial of 1 is 1
            return 1
        return self.solve(A - 1) * A

# Approach/Observation:-
# Factorial of a number N is the product of all numbers from 1 to N.
#
# Factorial can be calculated using following recursive formula.
#
# n! = n * (n-1)!
# n! = 1 if n = 0 or n = 1
#
# Note: Factorial of 0 is 1.
