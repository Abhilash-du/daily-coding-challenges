# Problem Description
# Given a string A denoting an expression. It contains the following operators '+', '-', '*', '/'.
# Check whether A has redundant braces or not.
# NOTE: A will be always a valid expression and will not contain any white spaces.
#
# Problem Constraints
# 1 <= |A| <= 105
#
# Input Format
# The only argument given is string A.
#
# Output Format
# Return 1 if A has redundant braces else, return 0.
#
# Example Input
# Input 1:  A = "((a+b))"
# Input 2:  A = "(a+(a+b))"
#
# Example Output
# Output 1:  1
# Output 2:  0
#
# Example Explanation
# Explanation 1:  ((a+b)) has redundant braces so answer will be 1.
# Explanation 2:  (a+(a+b)) doesn't have have any redundant braces so answer will be 0.

class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        operators = ['+', '-', '*', '/']
        ans = []
        for val in A:
            if val.isalpha():
                # if value is alphabetical then no need to add in stack
                continue
            elif val == '(' or val in operators:
                # if its opening braces, append it
                ans.append(val)
            else:
                # in case of closing braces
                if ans[-1] not in operators:
                    # if any operator is not found, return false / 1
                    return 1
                while ans[-1] != '(':
                    # remove all item from stack till open braces
                    ans.pop()
                ans.pop()  # remove open braces
        return 0
# Observation/Approach Followed:-
# We keep pushing operators and '(' onto the stack till we encounter ')'.
# When we encounter ')', we will check if operator is present on the top of stack
# After checking we will start popping operators until we find a matching '('.
# In case we not find any operator after each value ')' means it has redundant braces
# Otherwise, voila! Matching braces have been found.
