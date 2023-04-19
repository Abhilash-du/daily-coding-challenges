"""
1372. Longest ZigZag Path in a Binary Tree

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:

Choose any node in the binary tree and a direction (right or left).
If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
Change the direction from right to left or from left to right.
Repeat the second and third steps until you can't move in the tree.
Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.

Example:-
       1
      / \
     2   3
    / \   \
   4   5   6
      / \   \
     7   8   9

A ZigZag path can start from any node, so let's start from node 1 and choose the initial direction to be right.

 The path would be:

1 (length = 0) -> 3 (length = 1) -> 6 (length = 2) -> 9 (length = 3)

The length of this path is 3, which is the longest ZigZag path in the tree. Note that we started from node 1 and
chose the direction to be right initially. We moved to the right child of 1, then changed the direction to left and
moved to the right child of 3, then changed the direction to right and moved to the right child of 6, and finally
stopped as we couldn't move further.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max_len = None

    def longestZigZag(self, root: TreeNode) -> int:
        # Initialize a variable to keep track of the maximum length found so far
        self.max_len = 0

        # This function performs a depth-first search to find the maximum zig-zag length
        def solve(node_item, dir, curr_len):
            # Update the maximum length found so far
            self.max_len = max(self.max_len, curr_len)

            # If there is a left child, recursively call the function on it
            if node_item.left is not None:
                # If the current direction is right, update the current length and continue in the same direction
                if dir == 'right':
                    solve(node_item.left, 'left', curr_len + 1)
                # If the current direction is left, start a new zig-zag path with length 1
                else:
                    solve(node_item.left, 'left', 1)

            # If there is a right child, recursively call the function on it
            if node_item.right is not None:
                # If the current direction is left, update the current length and continue in the same direction
                if dir == 'left':
                    solve(node_item.right, 'right', curr_len + 1)
                # If the current direction is right, start a new zig-zag path with length 1
                else:
                    solve(node_item.right, 'right', 1)

            # Return the maximum length found so far
            return self.max_len

        # Call the function on the root node, with an empty direction and starting length of 0
        self.max_len = solve(root, '', 0)

        # Return the maximum length found
        return self.max_len


"""

Solution Approach:- 

This solution follows a recursive depth-first search approach to find the longest zig-zag path 
in a binary tree. 

The solve function takes three arguments - the current node, the direction of the previous step, 
and the current length of the zig-zag path. 

The function first updates the max_len variable with the maximum length 
found so far. Then, it recursively calls itself on the left and right child nodes of the current node, based on the 
current direction. 

If the current direction is left, the function calls itself on the right child node and updates 
the direction to right. Similarly, if the current direction is right, the function calls itself on the left child 
node and updates the direction to left. 

If there is no child node in the specified direction, the function ends the 
zig-zag path and returns the maximum length found so far.

The time complexity of this solution is O(n), where n is the number of nodes in the binary tree, since each node is 
visited once in the depth-first search. 

The space complexity is also O(n), since the depth of the recursion stack can be at most n in the worst case 
(in case of a skewed tree).
"""
