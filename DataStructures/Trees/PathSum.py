"""
Problem Description
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along
 the path equals the given sum.

Problem Constraints
1 <= number of nodes <= 10^5
-100000 <= B, value of nodes <= 100000

Input Format
First argument is a root node of the binary tree, A.
Second argument is an integer B denoting the sum.

Output Format
Return 1, if there exist root-to-leaf path such that adding up all the values along the path equals the given sum.
 Else, return 0.

Example Input
Input 1:

 Tree:    5
         / \
        4   8
       /   / \
      11  13  4
     /  \      \
    7    2      1

 B = 22
Input 2:

 Tree:    5
         / \
        4   8
       /   / \
     -11 -13  4

 B = -1

Example Output
Output 1: 1
Output 2: 0

Example Explanation
Explanation 1:

 There exist a root-to-leaf path 5 -> 4 -> 11 -> 2 which has sum 22. So, return 1.
Explanation 2:

 There is no path which has sum -1.
"""

# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A: root node of the tree
    # @param B: target sum
    # @return: an integer
    def hasPathSum(self, A, B):
        # If the current node is None, there is no path, so return 0.
        if A is None:
            return 0

        # If the current node is a leaf node (no children),
        # check if its value matches the target sum B.
        # Return 1 if there is a match, 0 otherwise.
        if A.left is None and A.right is None:
            return int(A.val == B)

        # Recursively check if there is a path with the target sum B
        # in the left and right subtrees.
        # Subtract the current node's value from the target sum B
        # to keep track of the remaining sum to be found.
        onLeft = self.hasPathSum(A.left, B - A.val)
        onRight = self.hasPathSum(A.right, B - A.val)

        # If there is a path with the target sum in either the left or right subtree,
        # return 1, otherwise return 0.
        return onLeft or onRight

"""

The approach followed in the hasPathSum function is a recursive depth-first search (DFS) on the binary tree.

The function takes two parameters: A represents the root node of the binary tree, and B represents the target sum we are
 looking for in the path.

Here's how the algorithm works:

1. If the current node A is None, it means we have reached a null node in the tree. In this case, there is no path, 
    so we  return 0.

2. If the current node A is a leaf node (i.e., it has no children), we check if its value A.val matches the target sum B
    If they are equal, it means we have found a path that sums up to B, so we return 1. Otherwise, we return 0.

3. If the current node A has both left and right children, we recursively check if there is a path with the target 
    sum in either the left subtree or the right subtree. To do this, we make two recursive calls:

        a) onLeft = self.hasPathSum(A.left, B - A.val): This checks if there is a path with the 
            remaining sum B - A.val in the left  subtree.

        b) onRight = self.hasPathSum(A.right, B - A.val): This checks if there is a path with the 
        remaining sum B - A.val in the right subtree.
        
4. Finally, we return onLeft or onRight, which indicates whether there is a path with the target sum B in either the 
    left or right subtree. If either of them returns 1, it means we found a path with the target sum, so we return 1. 
    Otherwise, we return 0.

The time complexity of this approach is O(N), where N is the number of nodes in the binary tree. 
This is because, in the worst case, we need to visit all nodes of the tree.

The space complexity is O(H), where H is the height of the binary tree. 
In the worst case, if the binary tree is skewed and resembles a linked list, 
the height H can be equal to the number of nodes N, resulting in O(N) space complexity. 
However, in a balanced binary tree, the height H is approximately log(N), leading to O(log(N)) space complexity.
"""