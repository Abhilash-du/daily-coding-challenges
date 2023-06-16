"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to determine the Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 Example 1:
Input: root = [1,7,0,7,-8,null,null]
Tree:-
          1
        /   \
       7     0
      / \
     7  -8

Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.


Constraints:
The number of nodes in the tree is in the range [1, 104].
-10^5 <= Node.val <= 10^5
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

from collections import deque


class Solution:
    def maxLevelSum(self, root) -> int:
        # Initialize an empty deque to use as a queue for BFS traversal
        queue = deque()
        queue.append(root)

        # Initialize level to 1 (level of the root node)
        level = 1

        # Initialize max_sum as negative infinity to track the maximum sum encountered
        max_sum = float('-inf')

        # Initialize ans to store the level with the maximum sum
        max_level = 0

        # Perform BFS traversal until the queue is empty
        while queue:
            # Initialize level_sum to 0 for the current level
            level_sum = 0

            # Get the number of nodes at the current level
            level_length = len(queue)

            # Process all nodes at the current level
            for _ in range(level_length):
                # Dequeue the front node from the queue
                node = queue.popleft()

                # Add the value of the current node to the level_sum
                level_sum += node.val

                # Enqueue the left and right children if they exist
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Check if the level_sum is greater than the current max_sum
            if level_sum > max_sum:
                # Update max_sum and max_level if a new maximum is found
                max_sum = level_sum
                max_level = level

            # Increment the level for the next iteration
            level += 1

        # Return the level with the maximum sum
        return max_level


"""
Intuition: We perform a breadth-first search (BFS) traversal to calculate the sum of nodes at each level.
We keep track of the maximum sum encountered and the level it corresponds to.

Time Complexity: The algorithm performs a BFS traversal, visiting each node once, resulting in O(N) time complexity,
where N is the number of nodes in the binary tree.

Space Complexity: The space complexity is determined by the maximum number of nodes at any level in the binary tree.
In the worst case, the queue can store all nodes at the last level, resulting in O(M) space complexity,
where M is the maximum number of nodes at any level in the binary tree.
"""
