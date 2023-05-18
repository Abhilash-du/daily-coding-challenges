"""
Problem Description
Given a binary search tree of integers. You are given a range B and C.
Return the count of the number of nodes that lie in the given range.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= B < = C <= 109

Input Format
First argument is a root node of the binary tree, A.
Second argument is an integer B.
Third argument is an integer C.

Output Format
Return the count of the number of nodes that lies in the given range.

Example Input
Input 1:

            15
          /    \
        12      20
        / \    /  \
       10  14  16  27
      /
     8

     B = 12
     C = 20
Input 2:

            8
           / \
          6  21
         / \
        1   7

     B = 2
     C = 20


Example Output
Output 1:

 5
Output 2:

 3

"""

# Definition for a binary tree node


# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A: root node of the tree
    # @param B: lower bound integer
    # @param C: upper bound integer
    # @return: an integer
    def solve(self, A, B, C):
        # Base case: if the current node is None, return 0
        if A is None:
            return 0

        # If the value of the current node is greater than the upper bound (C),
        # recursively explore the left subtree
        if A.val > C:
            return self.solve(A.left, B, C)

        # If the value of the current node is less than the lower bound (B),
        # recursively explore the right subtree
        if A.val < B:
            return self.solve(A.right, B, C)

            # If the value of the current node is within the range [B, C],
        # increment the count by 1 and recursively explore both left and right subtrees
        return 1 + self.solve(A.left, B, C) + self.solve(A.right, B, C)

"""
Solution Approach:-
The idea is to traverse the given binary search tree starting from the root.
For every node being visited, check if this node lies in range,
if yes, then add 1 to the result and recur for both of its children.
If the current node is smaller than the low value of the range, then recur for the right child; else recur for the left 
child.

Time Complexity (TC): O(N), where N is the number of nodes in the BST. We visit each node once.

Space Complexity (SC): O(H), where H is the height of the BST. The space is used for the recursive function call stack. 
"""