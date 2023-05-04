"""
Problem Description
Given a binary tree, return a 2-D array with vertical order traversal of it.
Go through the example for more details:-

Suppose we have the following binary tree:
        1
      /   \
     2     3
    / \   / \
   4   5 6   7

The vertical order traversal of this tree would be:
[
    [4],
    [2],
    [1, 5, 6],
    [3],
    [7]
]
NOTE: If 2 Tree Nodes shares the same vertical level then the one with lesser depth will come first.

Explanation:

The nodes 4, 2, and 1 are at vertical distance -2, -1, and 0 respectively.
The nodes 5 and 6 are at vertical distance 1.
The node 3 is at vertical distance 0.
The node 7 is at vertical distance 1.
So, the output array contains sub-arrays for each vertical distance, containing the nodes at that distance from the root


Problem Constraints
0 <= number of nodes <= 105



Input Format
First and only argument is a pointer to the root node of binary tree, A.



Output Format
Return a 2D array denoting the vertical order traversal of tree as shown.



Example Input=
Input 1:

      6
    /   \
   3     7
  / \     \
 2   5     9
Input 2:

      1
    /   \
   3     7
  /       \
 2         9


Example Output
Output 1:

 [
    [2],
    [3],
    [6, 5],
    [7],
    [9]
 ]
Output 2:

 [
    [2],
    [3],
    [1],
    [7],
    [9]
 ]


Example Explanation
Explanation 1: First row represent the verical line 1 and so on.

"""

from collections import deque


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verticalOrderTraversal(self, root):
        # Return empty list if tree is empty
        if not root:
            return []

        # Initialize variables
        min_val = float('inf')
        max_val = float('-inf')
        hmap = {}

        # Create a queue to store nodes and their levels
        q = deque([(root, 0)])
        while q:
            # Dequeue the node at the front of the queue and its level
            curr_node, curr_lvl = q.popleft()

            # Update the min_val and max_val variables
            min_val = min(min_val, curr_lvl)
            max_val = max(max_val, curr_lvl)

            # Add the node's value to the corresponding level in the hmap dictionary
            if curr_lvl not in hmap:
                hmap[curr_lvl] = []
            hmap[curr_lvl].append(curr_node.val)

            # Add the node's left and right children to the queue
            # with their corresponding levels
            if curr_node.left:
                q.append((curr_node.left, curr_lvl - 1))

            if curr_node.right:
                q.append((curr_node.right, curr_lvl + 1))

        # Create the result list by appending the values from the hmap dictionary
        # for each level in the range of min_val to max_val
        ans = []
        for i in range(min_val, max_val + 1):
            if i in hmap:
                ans.append(hmap[i])
        return ans


"""
Approach:

The approach used here is to perform a Breadth-First-Search (BFS) traversal of the binary tree using a queue, 
and keep track of the horizontal distance of each node from the root node. We use a dictionary/hashmap to store 
the node values at each horizontal distance. Then we iterate over the hashmap in order of increasing horizontal
 distance to construct the required 2D array.

Algorithm:

1. Initialize a queue with the root node and its horizontal distance as 0.
2. Initialize a dictionary to store the nodes' values for each horizontal distance.
3. While the queue is not empty, do the following:
    a. Pop the first node from the queue along with its horizontal distance.
    b. Update the minimum and maximum horizontal distance seen so far.
    c. If the horizontal distance is not present in the dictionary, create a new empty list for it.
    d. Append the node's value to the list corresponding to its horizontal distance in the dictionary.
    e. If the node has a left child, append it to the queue with its horizontal distance decreased by 1.
    f. If the node has a right child, append it to the queue with its horizontal distance increased by 1.
4. Iterate over the keys of the dictionary in ascending order and append the corresponding lists to the answer list.
5. Return the answer list.

Time complexity: The time complexity of the above algorithm is actually O(n), where n is the number of nodes in the 
binary tree. This is because we visit each node in the tree exactly once, and the operations within the while loop 
take constant time.

Space complexity:
The space complexity of the above algorithm is O(n), where n is the number of nodes in the binary tree. 
This is because we are using a dictionary/hashmap to store the nodes' values for each horizontal distance, 
which can contain n nodes at most. Additionally, we are using a queue to perform the BFS traversal,
 which can contain up to n nodes in the worst case.
"""