# Problem Description:
# Given the root of a tree A with each node having a certain value, find the count of nodes with
# more value than all its ancestor.
#
# Problem Constraints
# 1 <= Number of Nodes <= 200000
# 1 <= Value of Nodes <= 2000000000
#
# Input Format
# The first and only argument of input is a tree node.
#
# Output Format
# Return a single integer denoting the count of nodes that have more value than all of its ancestors.
# Example
# Input1: 3
# Input 2:
#     4
#    / \
#   5   2
#      / \
#     3   6
#
# Example Output
# Output 1: 1
# Output 2: 3
#
# Explanation 1:  There's only one node in the tree that is the valid node.
# Explanation 2:  The valid nodes are 4, 5 and 6.
#
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.count = 0

    def solve(self, A):

        def helper(root, max_val):
            if not root:
                return 0
            count = 0
            if root.val > max_val:
                max_val = root.val
                self.count += 1
            helper(root.left, max_val)
            helper(root.right, max_val)

        helper(A, -10)
        return self.count

# Solution Approach/Observation:-
#
# Run a DFS and keep track of the maximum so far.
#
# When arriving at a node, first find the answer for the left sub-tree,
# if it exists; then find the answer for the right sub-tree;
# Our current answer is the sum of both ans.
# But if the current node value is greater than max so far, we increment the answer.
#
# Note that since we keep track of max from above, it covers all nodes. Please look into complete solution for
# implementation.
