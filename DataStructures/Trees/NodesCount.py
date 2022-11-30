# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None
from collections import deque
import sys

sys.setrecursionlimit(10 ** 7 + 1)


class Solution:
    # @param A : root node of tree
    # @return an integer

    # Approach 1
    def solve(self, A):
        node = A
        queue = deque([node])
        count = 0
        while queue:
            val = queue.popleft()
            if val.left:
                queue.append(val.left)
            if val.right:
                queue.append(val.right)
            count += 1
        return count

    # Approach 2
    def recursiveSolve(self, A):
        if A is None:
            return 0
        count = 1
        count_left = self.recursiveSolve(A.left)
        count_right = self.recursiveSolve(A.right)
        return count + count_left + count_right

# We can solve this problem with two approaches:-
# Approach 1:
# We can use a queue to store the elements and its child an with each iteration
# count can be incremented
#
# Approach 2:
# Run a recursive function, call left and right children if they exist,
# and increase the answer variable accordingly.
