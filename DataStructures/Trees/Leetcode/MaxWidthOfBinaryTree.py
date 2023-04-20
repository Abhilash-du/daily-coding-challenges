"""

Given the root of a binary tree, return the maximum width of the given tree. The maximum width of a tree is the
maximum width among all levels. The width of one level is defined as the length between the end-nodes (the leftmost
and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary
tree extending down to that level are also counted into the length calculation. It is guaranteed that the answer will
in the range of a 32-bit signed integer.

Example1:-
Input: [1,3,2,5,3,null,9]
          1
        /   \
       3     2
      / \     \
     5   3     9

Output: 4
Explanation: The maximum width at level 3 is 4 (5,3,null,9).
         1
       /   \
  [0] 3     2 [1]
    / \     \
[0]5  3[N]   9 [2]

-----------------------------
Example 2:-
Input: [1,3,null,5,3]
          1
        /   \
       3   [N]
      / \
     5   3

Output: 2
Explanation: The maximum width at level 2 is 2 (5,3).
         1
       /   \
  [0] 3 [N] [1]
    / \
[0]5   3


Constraints:
The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100

"""
from collections import deque
class TreeNode:
    def __int__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # If the root is None, the tree has no width
        if not root:
            return 0

        # Create a queue to hold the nodes to be processed
        # Each element in the queue is a tuple consisting of a node and its index
        queue = deque([(root, 0)])

        # Initialize the maximum width seen so far to 0
        max_width = 0

        # Initialize the index seen so far to 0
        index = 0

        # Process the nodes in the queue until the queue is empty
        while queue:
            # Get the number of nodes in the current level and the index of the first node in the level
            level_length = len(queue)
            _, level_start = queue[0]

            # Process each node in the current level
            for i in range(level_length):
                # Remove the next node from the queue and get its index
                node, index = queue.popleft()

                # If the node has a left child, add it to the queue with its index doubled
                if node.left:
                    queue.append((node.left, index * 2))

                # If the node has a right child, add it to the queue with its index doubled plus 1
                if node.right:
                    queue.append((node.right, index * 2 + 1))

            # Compute the width of the current level and update max_width if necessary
            width = index - level_start + 1
            max_width = max(max_width, width)

        # Return the maximum width seen in the tree
        return max_width


"""

Approach: The approach taken by this algorithm is to perform a level-order traversal of the binary tree, 
keeping track of the index of each node in the tree. At each level of the tree, we compute the width of the level by 
subtracting the index of the first node in the level from the index of the last node in the level, and adding 1. We 
update a max_width variable with the maximum width seen so far, and return its value at the end.

To perform the level-order traversal, we use a queue to store the nodes at each level of the tree. We start by adding 
the root node and its index (which is 0) to the queue. Then, for each node in the queue, we add its left and right 
children to the queue with their indices calculated as 2*parent_index and 2*parent_index+1, respectively. We continue 
processing nodes in the queue until the queue is empty, at which point we have computed the maximum width of the tree.


Time Complexity: The time complexity of this algorithm is O(n), where n is the number of nodes in the binary tree. 
This is because we visit each node in the tree exactly once, and the operations performed at each node (adding its 
children to the queue and updating the max_width variable) take constant time.

Space Complexity: The space complexity of this algorithm is O(w), where w is the maximum width of the binary tree. 
This is because the size of the queue used to store nodes at each level of the tree is proportional to the width of 
the tree. In the worst case, where the tree is a complete binary tree, the width of the tree is approximately n/2, 
so the space complexity would be O(n).


"""
