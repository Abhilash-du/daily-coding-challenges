# Problem Description
# Given a Binary Tree A consisting of N integer nodes, you need to find the diameter of the tree.
# The diameter of a tree is the number of edges on the longest path between two nodes in the tree.
#
# Problem Constraints
# 0 <= N <= 105
#
# Input Format: First and only Argument represents the root of binary tree A.
#
# Output Format: Return an single integer denoting the diameter of the tree.
#
# Example Input
# Input 1:
#
#            1
#          /   \
#         2     3
#        / \
#       4   5
# Input 2:
#
#             1
#           /   \
#          2     3
#         / \     \
#        4   5     6
#
#
# Example Output
# Output 1:  3
# Output 2:  4
#
# Example Explanation
# Explanation 1:
# Longest Path in the tree is 4 -> 2 -> 1 -> 3 and the number of edges in this path is 3 so diameter is 3.
#
# Explanation 2:
# Longest Path in the tree is 4 -> 2 -> 1 -> 3 -> 6 and the number of edges in this path is 4 so diameter is 4.

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    ans = 0

    def diameter(self, A):
        if A is None:
            return 0
        lh = self.diameter(A.left)
        rh = self.diameter(A.right)
        self.ans = max(self.ans, lh + rh + 1)
        return 1 + max(lh, rh)

    def solve(self, A):
        self.diameter(A)
        return self.ans - 1
#
# First, let’s see how to find the height or maxDepth of a tree:
#
# If the tree is empty, then return 0
# Else
# (a) Get the max depth of each subtree recursively.
#
# (b) Take the max depth and second max depth of any subtree.
#       Get the max depth of the right subtree recursively, i.e., call height( tree->right-subtree)
#
# (c) Get the max of max depths of left and right subtrees and add 1 to it for the current node.
# max_depth = max(max dept of left subtree, max depth of right subtree) + 1
#
# (d) Return max_depth
#
# Diameter of a tree can be calculated by only using the height function,
# because the diameter of a tree is nothing but maximum value of (left_height + right_height + 1) for each node.
# So we need to calculate this value (left_height + right_height + 1) for each node and update the result.
# Time complexity – O(N).
