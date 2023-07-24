"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to find all possible full binary trees with 'n' nodes.

Problem Statement:-
Given an integer n, return a list of all possible full binary trees with n nodes.
Each node of each tree in the answer must have Node.val == 0.
Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.
A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Example1:
Input: n = 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Example 2:

Example2:
Input: n = 3
Output: [[0,0,0]]

Constraints:
1 <= n <= 20
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:

        # Dictionary to store previously computed full binary trees for a given number of nodes
        dp = {0: [], 1: [TreeNode(0)]}

        def generateFullBinaryTrees(num_nodes):
            # Check if the list of full binary trees for 'num_nodes' is already computed
            if num_nodes in dp:
                return dp[num_nodes]

            result = []

            # Divide the number of nodes into two parts: left subtree nodes and right subtree nodes
            for left_nodes in range(1, num_nodes):
                right_nodes = num_nodes - left_nodes - 1

                # Recursively generate all possible full binary trees for left and right subtrees
                left_subtrees = generateFullBinaryTrees(left_nodes)
                right_subtrees = generateFullBinaryTrees(right_nodes)

                # Combine left and right subtrees in all possible combinations to form full binary trees
                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        root_node = TreeNode(0, left_subtree, right_subtree)
                        result.append(root_node)

            # Store the computed list of full binary trees for 'num_nodes' in the dp dictionary
            dp[num_nodes] = result
            return dp[num_nodes]

        # Call the recursive function to generate all possible full binary trees for 'n' nodes
        return generateFullBinaryTrees(n)


"""
## Intuition
To efficiently solve the problem, I employed a dynamic programming approach to avoid redundant computations. 
I used recursion to generate all possible full binary trees for each number of nodes and stored the results in a 
dictionary for quick access. This approach significantly improved the efficiency of the solution.

## Time Complexity: The time complexity of the solution is optimized to O(n^2) since we avoid recomputing the same 
subproblems using the dynamic programming approach.
 The recursive nature of the algorithm contributes to the quadratic time complexity.

## Space Complexity: The space complexity of the solution is O(n^2) due to the dictionary used to store previously 
computed full binary trees for different numbers of nodes. The memory usage increases with the number of nodes, 
leading to quadratic space complexity.

"""