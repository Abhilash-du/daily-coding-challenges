"""
Problem Description
Given a binary tree,
Populate each next pointer to point to its next right node. If there is no next right node,
the next pointer should be set to NULL. Initially, all next pointers are set to NULL.

Assume perfect binary tree.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9

Input Format
First and only argument is head of the binary tree A.

Output Format
Return the head of the binary tree after the changes are made.

Example Input
Input 1:
     1
    /  \
   2    3

Input 2:
        1
       /  \
      2    5
     / \  / \
    3  4  6  7


Example Output
Output 1:
        1 -> NULL
       /  \
      2 -> 3 -> NULL

Output 2:
         1 -> NULL
       /  \
      2 -> 5 -> NULL
     / \  / \
    3->4->6->7 -> NULL

"""

from collections import deque


# Definition for a binary tree node
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root is None:
            return root

        # Create a queue to perform level order traversal
        q = deque([root, None])  # Initialize the queue with root and None (to mark the end of a level)

        while q:
            first_element = q.popleft()  # Get the first element from the queue

            if first_element is None:
                if q:
                    q.append(None)  # Add None to mark the end of the next level
            else:
                first_element.next = q[0]  # Set the next pointer to the first element in the queue

                if first_element.left:
                    q.append(first_element.left)  # Add the left child to the queue

                if first_element.right:
                    q.append(first_element.right)  # Add the right child to the queue

        return root


"""
Approach:
The approach used in this code is a modified level order traversal of the binary tree. The code utilizes a queue 
(implemented using deque) to perform the traversal. Starting with the root node, it iterates through each level of the 
tree and connects the nodes at the same level using the next pointer.

The algorithm initializes the queue with the root node and a None marker to represent the end of a level. 
It then enters a loop that continues until the queue is empty. In each iteration, it pops the first element from the 
queue. If the element is None, it indicates the end of a level, so a None marker is added to the queue if there are more
nodes to process. If the element is a valid node, it sets its next pointer to the first element in the queue
(which represents the next node at the same level). It also adds the left and right children of the current node to 
the queue if they exist).

By using this modified level order traversal, the algorithm connects the nodes at the same level by setting 
their next pointers.

Time Complexity:
The time complexity of this algorithm is O(N), where N is the number of nodes in the binary tree. 
This is because the algorithm visits each node once, and for each node, it performs constant-time operations such as 
appending to the queue and setting the next pointer.

Space Complexity:
The space complexity of this algorithm is O(M), where M is the maximum number of nodes at any level in the binary tree.
 In the worst case, the queue can store all the nodes at the deepest level of the tree, which can be at most M. 
 Therefore, the space required by the queue is proportional to the maximum number of nodes at any level.
"""
