"""
Problem Description
Given the root node of a Binary Tree denoted by A. You have to Serialize the given Binary Tree in the described format.
Serialize means encode it into a integer array denoting the Level Order Traversal of the given Binary Tree.

NOTE:
In the array, the NULL/None child is denoted by -1.
For more clarification check the Example Input.

Problem Constraints
1 <= number of nodes <= 105

Input Format
Only argument is a A denoting the root node of a Binary Tree.

Output Format
Return an integer array denoting the Level Order Traversal of the given Binary Tree.

Example Input
Input 1:

           1
         /   \
        2     3
       / \
      4   5
Input 2:

            1
          /   \
         2     3
        / \     \
       4   5     6

Example Output
Output 1: [1, 2, 3, 4, 5, -1, -1, -1, -1, -1, -1]
Output 2: [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1]


Example Explanation
Explanation 1:
 The Level Order Traversal of the given tree will be [1, 2, 3, 4, 5 , -1, -1, -1, -1, -1, -1].
 Since 3, 4 and 5 each has both NULL child we had represented that using -1.

Explanation 2:
 The Level Order Traversal of the given tree will be [1, 2, 3, 4, 5, -1, 6, -1, -1, -1, -1, -1, -1].
 Since 3 has left child as NULL while 4 and 5 each has both NULL child.
"""

# Importing the deque module from collections to use it for BFS
from collections import deque


# Defining a class called Solution
class Solution:

    # Defining a method called solve that takes the root node of a binary tree as input
    def solve(self, A):

        # Creating a deque with the root node as the starting element
        q = deque([A])

        # Creating a list to store the answer, initializing it with the value of the root node
        ans = [A.val]

        # Running a loop while the deque is not empty
        while (q):

            # Popping the leftmost element from the deque
            node = q.popleft()

            # Checking if the left child of the popped node exists
            if (node.left):

                # Adding the left child to the deque
                q.append(node.left)

                # Adding the value of the left child to the answer list
                ans.append(node.left.val)

            else:

                # If the left child does not exist, adding -1 to the answer list
                ans.append(-1)

            # Checking if the right child of the popped node exists
            if (node.right):

                # Adding the right child to the deque
                q.append(node.right)

                # Adding the value of the right child to the answer list
                ans.append(node.right.val)

            else:

                # If the right child does not exist, adding -1 to the answer list
                ans.append(-1)

        # Returning the answer list
        return ans


"""
Approach Followed:-
The approach used in this code is to perform a Breadth First Search (BFS) traversal of the binary tree.

First, a deque is initialized with the root node of the binary tree as the starting element. Then, a list called ans 
is initialized with the value of the root node.

In each iteration of the while loop, the leftmost element of the deque is popped and assigned to the variable node. 
The code then checks whether node has a left child. If it does, the left child is added to the deque and its value is 
appended to the ans list. If it does not, -1 is appended to ans in place of the missing child.

The code then checks whether node has a right child. If it does, the right child is added to the deque and its value 
is appended to the ans list. If it does not, -1 is appended to ans in place of the missing child.

The while loop continues until the deque is empty. Finally, the ans list is returned, which contains the level order 
traversal of the binary tree, with missing children represented by -1.

Overall, this approach effectively performs a BFS traversal of the binary tree and records the values of its nodes in 
level order. It also handles the case of missing children, which is important for correctly representing the binary 
tree as a list.

Time Complexity (TC): The code performs a BFS traversal of the binary tree, visiting each node exactly once. 
Therefore, the time complexity of the code is O(N), where N is the total number of nodes in the binary tree.

Space Complexity (SC): The space complexity of the code depends on the maximum size of the deque. In the worst case, 
the binary tree could be a complete binary tree with all leaf nodes at the same level. In this case, the maximum size 
of the deque would be (N/2)+1, where N is the total number of nodes in the binary tree. The ans list also has N 
elements. Therefore, the overall space complexity of the code is O(N)."""
