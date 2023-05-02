"""
Problem Description
You are given an integer array A denoting the Level Order Traversal of the Binary Tree.
You have to Deserialize the given Traversal in the Binary Tree and return the root of the Binary Tree.

NOTE:
In the array, the NULL/None child is denoted by -1.
For more clarification check the Example Input.

Problem Constraints
1 <= number of nodes <= 105
-1 <= A[i] <= 105

Input Format
Only argument is an integer array A denoting the Level Order Traversal of the Binary Tree.

Output Format
Return the root node of the Binary Tree.

Example Input
Input 1: A = [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
Input 2: A = [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1]

Example Output
Output 1:

           1
         /   \
        2     3
       / \
      4   5
Output 2:

            1
          /   \
         2     3
        / \ .   \
       4   5 .   6


Example Explanation:-
Explanation 1:

 Each element of the array denotes the value of the node. If the val is -1 then it is the NULL/None child.
 Since 3, 4 and 5 each has both NULL child we had represented that using -1.
Explanation 2:

 Each element of the array denotes the value of the node. If the val is -1 then it is the NULL/None child.
 Since 3 has left child as NULL while 4 and 5 each has both NULL child.

"""
# Importing the deque module from collections
from collections import deque
# Importing the sys module and setting the recursion limit to 1 million
import sys

sys.setrecursionlimit(10 ** 6)


# Definition of a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# The Solution class that contains the solve method to construct a binary tree
class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def solve(self, A):
        # Creating an empty deque to use as a queue
        q = deque()

        # Initializing variables for index and length of the input list
        i = 1
        n = len(A)

        # Creating the root node of the binary tree using the first element of the list
        root = TreeNode(A[0])

        # Assigning the root node to a variable that will be returned later
        ans = root

        # Adding the root node to the queue
        q.append(root)

        # Looping while there are still nodes in the queue and the end of the list has not been reached
        while q and i < n:
            # Removing the front node from the queue
            root = q.popleft()

            # Checking if the current element in the list represents a left child
            if A[i] != -1:
                # Creating a new node for the left child and adding it to the queue
                node_left = TreeNode(A[i])
                q.append(node_left)

                # Setting the left child of the current node to the new node
                root.left = node_left
            else:
                # If the current element in the list is -1, setting the left child of the current node to None
                root.left = None

            # Incrementing the index variable to process the next element in the list
            i += 1

            # Checking if the current element in the list represents a right child
            if A[i] != -1:
                # Creating a new node for the right child and adding it to the queue
                node_right = TreeNode(A[i])
                q.append(node_right)

                # Setting the right child of the current node to the new node
                root.right = node_right
            else:
                # If the current element in the list is -1, setting the right child of the current node to None
                root.right = None

            # Incrementing the index variable to process the next element in the list
            i += 1

        # Returning the root node of the binary tree
        return ans


"""

The provided code is used to construct a binary tree from a given list of integers. The approach used is to 
iterate through the list of integers and add nodes to the binary tree one by one. A deque is used as a queue to keep 
track of the nodes in the binary tree.

The root node of the binary tree is created from the first integer in the list, and added to the queue. Then, 
the while loop iterates over the queue until it is empty or until the end of the input list is reached. For each node 
in the queue, the code checks if the next two integers in the list correspond to the left and right children of the 
node. If there is a valid integer in the list, a new node is created and added to the queue, and its reference is set 
as the left or right child of the current node. If there is no valid integer in the list for the left or right child, 
the corresponding child of the current node is set to None.
Finally, the root node of the binary tree is returned as the output. 

The time complexity of this approach is O(N), where N is the number of nodes in the binary tree.

The space complexity of the provided code is O(N), where N is the number of nodes in the binary tree.

This is because the code uses a deque as a queue to keep track of the nodes in the binary tree. In the worst case, 
the deque can contain all the nodes of the binary tree, which is O(N) space. Additionally, the code creates a few 
temporary variables like node_left, node_right, and root, but the space used by these variables is negligible 
compared to the space used by the deque.

"""