"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the
 values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

"""


class Solution:
    def swapPairs(self, head):
        # Check if the head is empty or there is only one node
        if not head or not head.next:
            return head

        # Store the reference to the next node
        node = head.next

        # Recursively swap pairs starting from the third node
        head.next = self.swapPairs(node.next)

        # Swap the positions of the current node and the next node
        node.next = head

        # Return the new head node
        return node


"""
Intuition:
The code aims to swap adjacent nodes in a linked list pairwise. It uses a recursive approach to 
swap the nodes efficiently.

Approach:

1. The base case for the recursion is when the head is empty or there is only one node. In such cases, there is no need
    to swap, so the head is returned as it is.
2. For other cases, the code proceeds with swapping the pairs.
3. The code stores the reference to the next node (node) after the current head. This is done to connect the swapped
    pairs later.
4. The code recursively calls the swapPairs function on the next pair of nodes after the current pair. This swaps the 
    remaining nodes after the current pair.
5. The next pointer of the current head is set to the result of the recursive call, which will be the head of the 
    swapped pairs from the remaining nodes.
6. The next pointer of the current node (previously the second node in the pair) is set to the current head. 
    This effectively swaps the positions of the current node and the head.
7. The current node (node) is returned, which becomes the new head of the swapped pairs.

Time Complexity (TC):
The time complexity of the code is O(N), where N is the number of nodes in the linked list. This is because the code
 recursively swaps pairs of nodes until it reaches the end of the list. The recursion makes N/2 recursive calls, 
 resulting in a linear time complexity.

Space Complexity (SC):
The space complexity of the code is O(N), where N is the number of nodes in the linked list. 
This is because the recursion uses stack space proportional to the number of recursive calls made. 
In the worst case, if there are N/2 recursive calls, the space complexity is O(N).

"""
