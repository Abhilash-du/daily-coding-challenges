# Problem Description
# An arithmetic expression is given by a string array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.
# Valid operators are +, -, *, /. Each string may be an integer or an operator.
#
# Problem Constraints
# 1 <= N <= 105
#
# Input Format
# The only argument given is string array A.
#
# Output Format
# Return the value of arithmetic expression formed using reverse Polish Notation.
#
# Example Input
# Input 1: A =   ["2", "1", "+", "3", "*"]
# Input 2: A = ["4", "13", "5", "/", "+"]
#
# Example Output
# Output 1:  9
# Output 2:  6
#
# Example Explanation
# Explaination 1:
#     starting from backside:
#     * : () * ()
#     3 : () * (3)
#     + : (() + ()) * (3)
#     1 : (() + (1)) * (3)
#     2 : ((2) + (1)) * (3)
#     ((2) + (1)) * (3) = 9
# Explaination 2:
#     + : () + ()
#     / : () + (() / ())
#     5 : () + (() / (5))
#     13 : () + ((13) / (5))
#     4 : (4) + ((13) / (5))
#     (4) + ((13) / (5)) = 6

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        stack = []
        ans = int(A[0])  # incase length is 1
        for val in A:
            if val == "*" or val == "/" or val == "+" or val == "-":
                # pop the top two elements from the stack, perform the operation
                # and push that back into the stack
                if val == "/":
                    val = "//"
                val2 = stack.pop()
                val1 = stack.pop()
                ans = eval(val1 + val + val2)
                stack.append(str(ans))
            else:
                stack.append(val)
        return ans

# Solution Approach/Observation:-
# When you encounter an operator, that is when you need the top 2 numbers on the stack, perform the operation on them,
# and put them on the stack.
