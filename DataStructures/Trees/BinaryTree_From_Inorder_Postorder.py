"""
Problem Description
Given the inorder and postorder traversal of a tree, construct the binary tree.
NOTE: You may assume that duplicates do not exist in the tree.

Problem Constraints
1 <= number of nodes <= 105

Input Format
First argument is an integer array A denoting the inorder traversal of the tree.
Second argument is an integer array B denoting the postorder traversal of the tree.

Output Format
Return the root node of the binary tree.

Example Input
Input 1:
 A = [2, 1, 3]
 B = [2, 3, 1]

Input 2:
 A = [6, 1, 3, 2]
 B = [6, 3, 2, 1]

Example Output
Output 1:

   1
  / \
 2   3
Output 2:

   1
  / \
 6   2
    /
   3

Example Explanation 1: Create the binary tree and return the root node of the tree.
"""


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, InOrder, PostOrder):
        n = len(InOrder)
        # If the length of inorder traversal is 1, return a tree with the root node as that element
        if n == 1:
            return TreeNode(InOrder[0])

        # Create a dictionary with key-value pairs as node value-index
        # This will help to get the index of a node in constant time instead of linear search
        index_map = {val: i for i, val in enumerate(InOrder)}
        return self.buildBinaryTree(InOrder, PostOrder, 0, n - 1, 0, n - 1, index_map)

    def buildBinaryTree(self, InOrder, PostOrder, in_start, in_end, post_start, post_end, index_map):
        # If the index range is invalid, return None
        if in_start > in_end or post_start > post_end:
            return None

        # The last element of the postorder traversal is the root node
        val = PostOrder[post_end]
        root = TreeNode(val)

        # Get the index of the root node in the inorder traversal
        indx = index_map[val]

        # Calculate the number of nodes in the left subtree
        node_count = indx - in_start
        # Recursively build the left and right subtree of the root node
        root.left = self.buildBinaryTree(InOrder, PostOrder, in_start, in_start + node_count - 1, post_start,
                                         post_start + node_count - 1, index_map)
        root.right = self.buildBinaryTree(InOrder, PostOrder, in_start + node_count + 1, in_end,
                                          post_start + node_count, post_end - 1, index_map)

        # Return the root node
        return root


"""
Here are the steps followed in the approach:

    1. Create a dictionary called index_map to map the values in the inorder traversal to their corresponding indices.
    2. Call a recursive function called buildBinaryTree which takes in the following parameters:
        --> InOrder: the inorder traversal of the binary tree
        --> PostOrder: the postorder traversal of the binary tree
        --> in_start, in_end: the starting and ending indices of the inorder traversal
        --> post_start, post_end: the starting and ending indices of the postorder traversal
        --> index_map: the dictionary created in step 1
    3. If in_start is greater than in_end or post_start is greater than post_end, return None as the tree is empty.
    4. Get the root node of the tree from the last element in the postorder traversal, i.e., PostOrder[post_end].
    5. Find the index of the root node in the inorder traversal using index_map[PostOrder[post_end]] and store it in indx.
    6. Calculate the number of nodes in the left subtree using node_count = indx - in_start.
    7. Create a new node with the value of the root node, i.e., root = TreeNode(PostOrder[post_end]).
    8. Recursively build the left subtree by calling buildBinaryTree with the parameters:
        --> InOrder: the inorder traversal of the left subtree, i.e., InOrder[in_start:in_start+node_count]
        --> PostOrder: the postorder traversal of the left subtree, i.e., PostOrder[post_start:post_start+node_count]
        --> in_start: the starting index of the inorder traversal of the left subtree, i.e., in_start
        --> in_start+node_count-1: the ending index of the inorder traversal of the left subtree, i.e., in_start+node_count-1
        --> post_start: the starting index of the postorder traversal of the left subtree, i.e., post_start
        --> post_start+node_count-1: the ending index of the postorder traversal of the left subtree, 
            i.e., post_start+node_count-1
        --> index_map: the dictionary created in step 1
    9. Recursively build the right subtree by calling buildBinaryTree with the parameters:
        --> InOrder: the inorder traversal of the right subtree, i.e., InOrder[in_start+node_count+1:in_end+1]
        --> PostOrder: the postorder traversal of the right subtree, i.e., PostOrder[post_start+node_count:post_end]
        --> in_start+node_count+1: the starting index of the inorder traversal of the right subtree, 
            i.e., in_start+node_count+1
        --> in_end: the ending index of the inorder traversal of the right subtree, i.e., in_end
        --> post_start+node_count: the starting index of the postorder traversal of the right subtree, 
            i.e., post_start+node_count
        --> post_end-1: the ending index of the postorder traversal of the right subtree, i.e., `post_end
    

Time Complexity:
The time complexity of the solution is O(n), where n is the number of nodes in the tree. This is because we 
process each node in the tree exactly once.

Space Complexity:
The space complexity of the  solution is also O(n), because we use a dictionary to store the indices of the 
elements in the inorder list, which takes up O(n) space. Additionally, the recursive calls to the buildBinaryTree 
function also take up space on the call stack, but the maximum depth of the call stack is O(n) for a binary tree with 
n nodes. Therefore, the overall space complexity is O(n).
"""
