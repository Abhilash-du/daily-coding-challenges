"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine  all the structurally unique BST's
# PROBLEM URL: https://leetcode.com/problems/unique-binary-search-trees-ii/description/

Given an integer n, return all the structurally unique BST's (binary search trees), which has exactly n nodes of unique
 values from 1 to n. Return the answer in any order.

Example 1:
Input: n = 3
Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

Example 2:
Input: n = 1
Output: [[1]]
"""
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import sys

sys.setrecursionlimit(10 ** 6)


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}  # A dictionary to store computed results for subproblems

        def generateSubtrees(start, end):
            # Base case: if start > end, return a list with a single element 'None'
            if start > end:
                return [None]

            # If the current subproblem has been computed before, return the result from dp
            if (start, end) in dp:
                return dp[(start, end)]

            result = []  # List to store the generated subtrees for the current subproblem

            # Try each value from 'start' to 'end' as the root of the current subtree
            for root_value in range(start, end + 1):
                # Generate all possible left subtrees for the current root value
                for left_subtree in generateSubtrees(start, root_value - 1):
                    # Generate all possible right subtrees for the current root value
                    for right_subtree in generateSubtrees(root_value + 1, end):
                        # Create a new tree node with the current root value and its left and right subtrees
                        root_node = TreeNode(root_value, left_subtree, right_subtree)
                        result.append(root_node)

            # Store the computed result in dp for future reference and return the result
            dp[(start, end)] = result
            return result

        return generateSubtrees(1, n)

