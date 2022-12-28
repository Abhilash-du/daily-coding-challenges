class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        stack = []
        while A:
            val = A.pop()
            while stack and stack[-1] > val:
                # top value of stack is greater than current value of A, add it to the end
                A.append(stack.pop())
            stack.append(val)
        return stack

# Solution Approach:-
# Create a temporary stack
#
# While input stack is not empty:
# 1. pop an element from input stack calls it val.
# 2. while the temporary stack is not empty and top of the
# temporary stack is greater than val pop from the temporary stack and push it into input stack.
# 3. push val in the temporary stack.
#
# The sorted numbers are in the temporary stack.
# Worst case time complexity O(n^2).
