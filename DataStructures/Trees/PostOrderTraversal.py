# Problem Description
# Given a binary tree, return the Postorder traversal of its nodes values.
# NOTE: Using recursion is not allowed.
#
# Problem Constraints
# 1 <= number of nodes <= 105
#
# Input Format
# First and only argument is root node of the binary tree, A.
#
# Output Format
# Return an integer array denoting the Postorder traversal of the given binary tree.
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
# Output 1:  [3, 2, 1]
# Output 2:  [6, 3, 2, 1]
#
# Example Explanation
# Explanation 1:  The Preoder Traversal of the given tree is [3, 2, 1].
# Explanation 2:  The Preoder Traversal of the given tree is [6, 3, 2, 1].

# Definition for a  binary tree node
# class TreeNode:
#   def __init__(self, x):
#       self.val = x
#       self.left = None
#       self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal_app1(self, A):
        stack = []
        ans = []
        while stack or A is not None:
            if A is not None:
                # append all left value in stack
                stack.append(A)
                A = A.left
            else:
                if stack[-1].right is not None:
                    # if A has right child
                    A = stack[-1].right
                else:
                    # if A has no right child
                    element = stack.pop()
                    ans.append(element.val)

                    while stack and stack[-1].right is element:
                        # if pending stack items has no right child
                        element = stack.pop()
                        ans.append(element.val)
        return ans

    # Approach#2:-
    def postorderTraversal_app2(self, A):
        stack = [A]
        ans = []
        while stack:
            top = stack.pop()
            ans.append(top.val)
            if top.left:
                stack.append(top.left)
            if top.right:
                stack.append(top.right)
        return ans[::-1]

# Observation/Approach followed:-
#
# Recursive call would look something like this :
#
#   postorderprint(root->left);
#   postorderprint(root->right);
#   print(root->val);
#
# Instead of calling the functions, we can put the nodes on a stack and process them
