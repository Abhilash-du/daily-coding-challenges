"""
Problem Description
Given a binary tree of integers denoted by root A. Return an array of integers representing the top view of the Binary tree.
The top view of a Binary Tree is a set of nodes visible when the tree is visited from the top.

Return the nodes in any order.

Problem Constraints
1 <= Number of nodes in binary tree <= 100000
0 <= node values <= 10^9

Input Format
First and only argument is head of the binary tree A.

Output Format
Return an array, representing the top view of the binary tree.

Input 1:
            1
           / \
          2   3
         / \ / \
        4  5 6  7

Output1: [1, 2, 4, 3, 7]

Example Explanation 1: Top view is described.
"""

from collections import deque


class Solution:
    def __init__(self):
        self.min_val = int(float('inf'))  # Initialize the minimum horizontal distance to infinity
        self.max_val = int(-float('inf'))  # Initialize the maximum horizontal distance to negative infinity

    def solve(self, A):
        hmap = {}  # Initialize an empty dictionary to store nodes at each horizontal distance
        hmap = self.createLevelHmap(A)  # Create a level-wise dictionary of nodes in the binary tree
        ans = []
        # Iterate over the horizontal distances between the minimum and maximum values
        for i in range(self.min_val, self.max_val + 1):
            ans.append(hmap[i][0])  # Append the first node at each horizontal distance to the answer list

        return ans

    def createLevelHmap(self, A):
        hmap = {}  # Initialize an empty dictionary to store nodes at each horizontal distance
        q = deque([])  # Initialize a queue to perform a level-order traversal
        q.append((A, 0))  # Add the root node with horizontal distance 0 to the queue

        # Perform a level-order traversal of the binary tree
        while (q):
            pair = q.popleft()  # Remove the next node from the queue
            node = pair[0]  # Extract the node from the pair
            index = pair[1]  # Extract the horizontal distance from the pair
            self.min_val = min(self.min_val, index)  # Update the minimum horizontal distance
            self.max_val = max(self.max_val, index)  # Update the maximum horizontal distance
            # Add the node to the dictionary at the corresponding horizontal distance
            if index in hmap:
                hmap[index].append(node.val)
            else:
                hmap[index] = [node.val]
            # Add the left and right children of the node to the queue with the updated horizontal distance
            if node.left:
                q.append((node.left, index - 1))
            if node.right:
                q.append((node.right, index + 1))

        return hmap


"""
The approach of this solution is to use a hash map to keep track of the nodes seen at each vertical level of the 
tree. We will use a deque data structure to traverse the tree level-by-level. For each node, we will also keep track 
of its vertical level (i.e., horizontal distance from the root), so that we can store the node in the corresponding 
level of the hash map.

To obtain the top view of the tree, we need to output the first node encountered at each vertical level. To achieve 
this, we can simply iterate over the range of vertical levels seen in the tree, and append the first node encountered 
at each level to our result array.

Time Complexity:
The time complexity of this solution is O(N), where N is the number of nodes in the binary tree. This is because we 
are traversing the tree level-by-level, visiting each node exactly once. 

Space Complexity:
The space complexity of this solution is 
also O(N), because in the worst case, we may need to store all nodes at the same vertical level in the hash map.
"""