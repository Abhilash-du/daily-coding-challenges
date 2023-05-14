"""
Problem Description
Given a binary tree, return the zigzag level order traversal of its nodes values. (ie, from left to right,
then right to left for the next level and alternate between).



Problem Constraints
1 <= number of nodes <= 105



Input Format
First and only argument is root node of the binary tree, A.



Output Format
Return a 2D integer array denoting the zigzag level order traversal of the given binary tree.



Example Input
Input 1:

    3
   / \
  9  20
    /  \
   15   7
Input 2:

   1
  / \
 6   2
    /
   3


Example Output
Output 1:

 [
   [3],
   [20, 9],
   [15, 7]
 ]
Output 2:

 [
   [1]
   [2, 6]
   [3]
 ]
Example Explanation
Explanation 1:

 Return the 2D array. Each row denotes the zigzag traversal of each level.

"""

# Import the deque module from collections
from collections import deque


# Define a class called Solution
class Solution:
    # Define a function called zigzagLevelOrder that takes in a binary tree node as input
    # and returns a list of lists of integers
    def zigzagLevelOrder(self, A):
        # Initialize a deque with the root node of the tree and a None value
        q = deque([A, None])
        # Initialize two empty lists, one to store the answer and one to temporarily store nodes
        ans = []
        tmp = []
        # Initialize a flag to indicate whether to reverse the order of nodes in the current level
        opposite_flag = True

        # Continue the loop while the deque is not empty
        while (q):
            # Remove the leftmost element from the deque
            top_element = q.popleft()
            # If the element is not None, add its value to the temporary list and add its children to the deque
            if (top_element is not None):
                tmp.append(top_element.val)
                if (top_element.right):
                    q.append(top_element.right)
                if (top_element.left):
                    q.append(top_element.left)
            # If the element is None, it means we've finished processing a level of the tree
            else:
                # If the temporary list is not empty, add it to the answer list and reset the temporary list
                if (tmp):
                    # If the flag is True, reverse the order of nodes in the list before adding it to the answer
                    if (opposite_flag == True):
                        ans.append(tmp[::-1])
                        opposite_flag = False
                    # If the flag is False, add the nodes to the answer as-is
                    else:
                        ans.append(tmp)
                        opposite_flag = True
                    tmp = []
                # If the deque is not empty, add another None value to indicate the end of the next level
                if (q):
                    q.append(None)
        # Return the answer list
        return ans


"""
Approach Followed:-
The function uses a deque data structure to keep track of the nodes in the tree. Initially, the deque contains the 
root node of the tree and a None value to indicate the end of the first level. We also initialize two empty lists, 
ans to store the final answer, and tmp to temporarily store the nodes of each level.

We then enter a while loop that continues until the deque is empty. In each iteration, we remove the leftmost 
element from the deque and check if it is a node or the end of a level (indicated by the None value). If it is a 
node, we add its value to the tmp list and add its children to the deque. If it is the end of a level, we add the 
tmp list to the ans list in reverse order if the flag opposite_flag is True, and in the original order if the flag 
is False. We then reset the tmp list and add another None value to the deque to indicate the end of the next level.

Finally, we return the ans list, which contains the node values in a zigzag level order.

Time Complexity Analysis: 
The time complexity of the function zigzagLevelOrder is O(N), where N is the total number
of nodes in the tree. This is because we need to visit every node in the tree once in the worst case.

Space Complexity Analysis: 
The space complexity of the function zigzagLevelOrder is O(W), where W is the maximum 
width of the tree (i.e., the maximum number of nodes at any level of the tree). This is because we need to store 
the nodes of each level in the tmp list, which can have a maximum of W nodes. Additionally, we use the deque to 
keep track of the nodes, which can also have a maximum of W nodes at any point. Therefore, the space complexity of 
the function is O(W)."""
