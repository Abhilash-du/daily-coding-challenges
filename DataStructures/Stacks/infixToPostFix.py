# Problem Description
# Given string A denoting an infix expression. Convert the infix expression into a postfix expression.
# String A consists of ^, /, *, +, -, (, ) and
# lowercase English alphabets where lowercase English alphabets are operands and ^, /, *, +, - are operators.
#
# Find and return the postfix expression of A.
# NOTE:-
# ^ has the highest precedence.
# / and * have equal precedence but greater than + and -.
# + and - have equal precedence and lowest precedence among given operators.
#
# Problem Constraints
# 1 <= length of the string <= 500000
#
# Input Format
# The only argument given is string A.
#
# Output Format
# Return a string denoting the postfix conversion of A.
#
# Example Input
# Input 1:  A = "x^y/(a*z)+b"
# Input 2:  A = "a+b*(c^d-e)^(f+g*h)-i"
#
# Example Output
# Output 1:  "xy^az*/b+"
# Output 2:  "abcd^e-fgh*+^*+i-"
#
# Example Explanation
# Explanation 1:  Ouput dentotes the postfix expression of the given input.

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        priority = {
            '^': 3, '/': 2, '*': 2, '+': 1, '-': 1
        }
        stack = []
        ans = ""
        for i in range(n):
            val = A[i]
            if val.isalpha():
                # If the scanned character is an operand, add it to output string.
                ans += val
            elif val == '(':
                # If the scanned character is an ‘(‘, append it to the stack.
                stack.append(val)
            elif val == ')':
                # If the scanned character is an ‘)’, pop and to output string from the stack
                # until an ‘(‘ is encountered.
                while stack[-1] != '(':
                    ans += stack.pop()
                stack.pop()
            elif val in priority:
                if len(stack) == 0 or stack[-1] == '(':
                    stack.append(val)
                else:
                    while stack and priority[val] <= priority[stack[-1]]:
                        ans += stack.pop()
                        if len(stack) > 0 and stack[-1] == "(":
                            break
                    stack.append(val)
        while stack:
            # Pop all the remaining elements from the stack
            ans += stack.pop()
        return ans

# Observation/Approach Followed:-
# Algorithm:
# 1. Scan the infix expression from left to right.
# 2. If the scanned character is an operand, output it.
# 3. Else,
#   3.1 If the precedence of the scanned operator is greater than that of the operator in the stack
#   (or the stack is empty, or the stack contains a ‘(‘ ), push it.
#   3.2 Else, Pop all the operators from the stack which are greater than or equal to in precedence than
#   that of the scanned operator. After doing that, Push the scanned operator to the stack.
#   (If you encounter parenthesis while popping, stop there and push the scanned operator in the stack.)
# 4. If the scanned character is an ‘(‘, push it to the stack.
# 5. If the scanned character is an ‘)’, pop the stack and output it until a ‘(‘ is encountered,
#   and discard both the parenthesis.
# 6. Repeat steps 2-6 until infix expression is scanned.
# 7. Print the output
# 8. Pop and output from the stack until it is not empty.
