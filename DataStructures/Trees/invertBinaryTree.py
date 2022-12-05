# Problem Description
# Given a binary tree A, invert the binary tree and return it.
#
# Inverting refers to making the left child the right child and vice versa.
#
# Problem Constraints
# 1 <= size of tree <= 100000
#
# Input Format
# First and only argument is the head of the tree A.
#
# Output Format
# Return the head of the inverted tree.
#
# Input1:-
#      1
#     / \
#     2  3
#
# Input 2:-
#      1
#    /   \
#   2     3
#  / \   / \
# 4   5 6   7
#
# Output 1:
#      1
#    /   \
#   3     2
#
# Output 2:
#      1
#    /   \
#   3     2
#  / \   / \
# 7   6 5   4

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        if A is None:
            return
        self.invertTree(A.left)
        self.invertTree(A.right)
        A.left, A.right = A.right, A.left
        return A

# Solution Approach/Observation:-
# Think recursively.
# You need to invert the left and right subtree on every node and then swap them.
