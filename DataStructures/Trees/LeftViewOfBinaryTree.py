"""
Problem Description
Given a binary tree of integers. Return an array of integers representing the left view of the Binary tree.
Left view of a Binary Tree is a set of nodes visible when the tree is visited from Left side
NOTE: The value comes first in the array which have lower level.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 109

Input Format
First and only argument is a root node of the binary tree, A.

Output Format
Return an integer array denoting the left view of the Binary tree.

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
Output 1: [1, 2, 4, 8]
Output 2: [1, 2, 4, 5]

Example Explanation:-
Explanation 1: The Left view of the binary tree is returned.
"""
# Definition for a binary tree node
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def solve(self, A):
        # initialize a deque with None and the root node of the tree
        q = deque([None, A])

        # initialize an empty list to store the left view of the binary tree
        ans = []

        # iterate until the queue is not empty
        while q:
            # dequeue the first node from the queue
            curr_node = q.popleft()

            # if the dequeued node is not None
            if curr_node is not None:
                # if the dequeued node has a left child, add it to the queue
                if curr_node.left:
                    q.append(curr_node.left)

                # if the dequeued node has a right child, add it to the queue
                if curr_node.right:
                    q.append(curr_node.right)

            # if the dequeued node is None
            else:
                # if the queue is not empty, the next node in the queue is the leftmost node of the current level
                if len(q) > 0:
                    ans.append(q[0].val)
                    # add None to the queue to mark the end of the current level
                    q.append(None)

        # return the list containing the left view of the binary tree
        return ans


"""
Approach Followed:- 

The intuition behind the given code is to perform a level order traversal of the binary tree 
and keep track of the leftmost node of each level.

We use a deque data structure to implement a level order traversal. We start by inserting None and the root node into 
the deque. We then iterate over the deque until it is empty. In each iteration, we dequeue a node from the left end of
the deque. If the dequeued node is not None, we check if it has any left or right child, and if it does, we enqueue 
them at the right end of the deque. If the dequeued node is None, it means we have finished traversing the current 
level of the binary tree, and the next node in the deque would be the leftmost node of the next level. So, we add the
 value of the next node in the deque to the answer list.

In this way, we keep traversing the binary tree level by level until the deque becomes empty, and we have recorded the 
leftmost node of each level in the answer list.

The time complexity of the algorithm is O(N), where N is the number of nodes in the binary tree. This is because we 
traverse each node of the binary tree once using a level order traversal, and the time complexity of each operation 
(dequeue, enqueue, and append to the answer list) is O(1) using a deque data structure.

The space complexity of the algorithm is also O(N), as in the worst case scenario, the deque would contain all the nodes
of the last level of the binary tree.
"""
