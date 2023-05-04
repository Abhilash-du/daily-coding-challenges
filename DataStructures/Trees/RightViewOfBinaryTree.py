"""

Problem Description Given a binary tree of integers denoted by root A. Return an array of integers representing
the right view of the Binary tree. Right view of a Binary Tree is a set of nodes visible when the tree is visited
from Right side.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9

Input Format
First and only argument is head of the binary tree A.

Output Format
Return an array, representing the right view of the binary tree.

Example Input
Input 1:
            1
          /   \
         2    3
        / \  / \
       4   5 6  7
      /
     8

Input 2:
            1
           /  \
          2    3
           \
            4
             \
              5


Example Output
Output 1:  [1, 3, 7, 8]
Output 2:  [1, 3, 4, 5]


Example Explanation:-
Explanation 1:Right view is described.
Explanation 2:Right view is described.

"""

# Importing deque from collections module
from collections import deque


# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # Function to return a list of integers in the order of the last node in each level of a binary tree
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, root):
        # Initializing a deque with None and root
        q = deque([None, root])
        # Initializing an empty list to store the values of the last node in each level
        ans = []
        # Loop until the deque is not empty
        while q:
            # Pop the first node from the deque
            first_node = q.popleft()
            # If the first node is not None
            if first_node is not None:
                # If the first node has a right child, add it to the deque
                if first_node.right:
                    q.append(first_node.right)
                # If the first node has a left child, add it to the deque
                if first_node.left:
                    q.append(first_node.left)
            # If the first node is None
            else:
                # If there are more nodes in the deque, add the value of the first node in the next level to the ans
                # list
                if len(q) >= 1:
                    ans.append(q[0].val)
                    # Add a None node to the deque to mark the end of the next level
                    q.append(None)
        # Return the list of values of the last node in each level
        return ans


"""
Approach Followed:-
This algorithm is used to obtain the values of the rightmost node in each level of a binary tree. The approach is 
based on a modified level-order traversal of the binary tree using a queue.

We can start by initializing a deque with None and the root node of the binary tree. We use None as a delimiter to 
separate the levels of the binary tree in the deque. We also initialize an empty list ans to store the values of the 
rightmost node in each level.

We then start a loop that continues until the deque is empty. At each iteration, we pop the first node from the left 
of the deque. If the node is not None, we add its right child and left child to the deque, if they exist. This 
ensures that we process all the nodes in a level before moving to the next level.

If the node is None, we know that we have reached the end of a level, and the next node in the deque must be the 
first node in the next level. Therefore, we append the value of the first node in the next level to the ans list, 
and we add a None node to the deque to mark the end of the next level.

Finally, we return the ans list containing the values of the rightmost node in each level of the binary tree.

This algorithm has a time complexity of O(n), where n is the number of nodes in the binary tree, because we process 
each node exactly once. The space complexity of the algorithm is O(n), because the deque can contain at most two 
levels of nodes at any point in time.

"""
