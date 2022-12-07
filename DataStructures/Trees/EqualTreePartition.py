# Problem Description:-
# Given a binary tree A.
# Check whether it is possible to partition the tree to two trees which have equal sum of values after removing exactly
# one edge on the original tree.
#
# Problem Constraints
# 1 <= size of tree <= 100000
# 0 <= value of node <= 10**9
#
# Input Format
# First and only argument is head of tree A.
#
# Output Format
# Return 1 if the tree can be partitioned into two trees of equal sum else return 0.
#
# Example Input
# Input 1:
#           5
#         /    \
#         3     7
#        / \   / \
#       4   6  5  6
#
# Input2:
#           1
#          /  \
#         2   10
#             / \
#            20  2
#
# Example Output
# Output 1:  1
# Output 2: 0

import sys

sys.setrecursionlimit(10 ** 5)


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

    def findSum(self, current_node, target):
        # returns sum and updates if target sum is achieved
        if current_node is None:
            return 0
        sum_val = current_node.val + self.findSum(current_node.left, target) + self.findSum(current_node.right, target)
        if sum_val == target:
            # if target element is found
            self.ans = 1
        return sum_val

    def solve(self, A):
        total_sum = self.findSum(A, 10 ** 7 + 3)  # finding the total sum of nodes
        self.ans = 0
        if total_sum & 1 is 1:
            # if total sum is odd then it cannot be subdivided further
            return 0
        self.findSum(A, total_sum // 2)  # checks if the tree can be divided into two equal node sums
        return self.ans
#
# Solution Approach/Observation:-
# After removing some edge from parent to child,
# (where the child cannot be the original root)
# the subtree rooted at child must be half the sum of the entire tree.
#
# Let’s record the sum of every subtree. We can do this recursively using depth-first search.
# After, we should check that half the sum of the entire tree occurs somewhere in our recording
# (and not from the total of the entire tree.)
