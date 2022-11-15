# Problem Description
# Given an expression string A, examine whether the pairs and the orders of “{“,”}”, ”(“,”)”, ”[“,”]” are correct in A.
# Refer to the examples for more clarity.
#
# Problem Constraints
# 1 <= |A| <= 100
#
# Input Format
# The first and the only argument of input contains the string A having the parenthesis sequence.
#
# Output Format
# Return 0 if the parenthesis sequence is not balanced.
# Return 1 if the parenthesis sequence is balanced.
#
# Example Input
# Input 1:  A = {([])}
# Input 2:  A = (){
# Input 3:  A = ()[]
#
# Example Output
# Output 1:  1
# Output 2:  0
# Output 3:  1
#
# Example Explanation
# You can clearly see that the first and third case contain valid parenthesis.
# In the second case, there is no closing bracket for {, thus the parenthesis sequence is invalid.

class Solution:
    def solve(self, A):
        stack = []
        for val in A:
            if val == "{" or val == "[" or val == "(":
                # push any opening bracket into the stack
                stack.append(val)
            else:
                # check if the last unpaired opening bracket is of the same type
                # as the current closing bracket
                if not stack:
                    return 0
                if val == "}":
                    if stack[-1] != "{":
                        return 0
                    else:
                        stack.pop()
                if val == "]":
                    if stack[-1] != "[":
                        return 0
                    else:
                        stack.pop()
                if val == ")":
                    if stack[-1] != "(":
                        return 0
                    else:
                        stack.pop()
        # checks if all the opening brackets are paired
        if stack:
            return 0
        return 1

# Observation/Approach Followed:-
# First, let us look at the impossible cases:
# 1) [() : There is no corresponding closing bracket for an opening bracket.
# 2) [) : Incorrect closing bracket for an opening bracket.
# 3) } : No opening bracket for a closed bracket.
#
# Now, we can observe that the earlier a bracket is encountered in the string, the later it is closed.
# We can guess that the Stack Data Structure will be used using this observation.
#
# We traverse the given string from the left. If the i-th character is an opening bracket, we push it onto the stack.
# If it is a closing bracket, we check for the impossible case 2 and case 3. If they are being violated, then we can
# simply return 0. Otherwise, we can pop the topmost bracket from the stack. To check for case 1, if our stack is not
# empty at the end of our traversal, then we can say that the brackets are not correctly matched.
#
# If all the conditions are fulfilled, then we can return 1.