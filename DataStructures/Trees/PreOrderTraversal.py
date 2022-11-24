# Problem Description
# Given a binary tree, return the preorder traversal of its nodes values.
# NOTE: Using recursion is not allowed.
#
# Problem Constraints
# 1 <= number of nodes <= 105
#
# Input Format
# First and only argument is root node of the binary tree, A.
#
# Output Format
# Return an integer array denoting the preorder traversal of the given binary tree.
#
# Example Input
# Input 1:
#
#    1
#     \
#      2
#     /
#    3
# Input 2:
#
#    1
#   / \
#  6   2
#     /
#    3
#
#
# Example Output
# Output 1:  [1, 2, 3]
# Output 2:  [1, 6, 2, 3]
#
#
# Example Explanation
# Explanation 1:  The Preoder Traversal of the given tree is [1, 2, 3].
# Explanation 2:  The Preoder Traversal of the given tree is [1, 6, 2, 3].


# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        stack = []
        ans = []
        while A is not None or stack:
            if A is not None:
                stack.append(A.right)
                ans.append(A.val)
                A = A.left
            else:
                A = stack.pop()
        return ans

# Solution Approach/Observation:-
# We can do this problem easily with recursion, but recursion is not allowed here.
# # Stack can help to avoid recursion. Think about using Stack.
#
# Recursive call would look something like this :
# print(root->val);
# preorderprint(root->left);
# preorderprint(root->right);
#
# Instead of calling the functions, can you put the nodes on a stack and process them?
