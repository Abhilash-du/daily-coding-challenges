"""
1721. Swapping Nodes in a Linked List
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from
the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]

Constraints:
The number of nodes in the list is n.
1 <= k <= n <= 10^5
0 <= Node.val <= 100
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head, k):
        # Initialize two pointers, fast and slow, to the head of the linked list
        fast = head
        slow = head

        # Move the fast pointer k-1 positions ahead
        for i in range(k - 1):
            fast = fast.next

        # Keep track of the node at position k (first) and the node after k (fast)
        first = fast
        fast = fast.next

        # Move the slow and fast pointers together until the fast pointer reaches the end of the list
        while fast:
            slow, fast = slow.next, fast.next

        # Swap the values of the nodes at positions k and (length-k+1)
        first.val, slow.val = slow.val, first.val

        # Return the head of the modified linked list
        return head

"""
Intuition
The task is to swap the values of two nodes in a linked list based on their positions. The approach is to traverse the 
linked list and find the nodes at positions k and (length-k+1). Then, swap the values of these nodes.
The slow and fast pointer approach is used to efficiently find two nodes in a linked list that need to be swapped based 
on their positions. By using two pointers, one moving at a slower pace (slow) and the other moving at a faster pace 
(fast), we can identify the desired nodes.

Approach
Initialize two pointers, fast and slow, to the head of the linked list.
Move the fast pointer k-1 positions ahead. This positions the fast pointer at the kth node.
Keep track of the node at position k (first) and the node after k (fast).
Move the slow and fast pointers together until the fast pointer reaches the end of the list. This positions the 
slow pointer at the (length-k+1)th node.
Swap the values of the nodes at positions k and (length-k+1) by swapping first.val and slow.val.
Return the head of the modified linked list.
By utilizing the slow and fast pointer technique, we avoid the need to traverse the linked list multiple times and can 
swap the nodes efficiently in a single pass.

The slow and fast pointer approach is commonly used in linked list problems that require finding a particular node or 
solving problems based on positions within the list.

Complexity
Time complexity:
The time complexity of the code is O(n), where n is the number of nodes in the linked list. This is because we need to 
traverse the linked list once to find the nodes at positions k and (length-k+1).

Space complexity:
The space complexity of the code is O(1) because we are using a constant amount of extra space to store the pointers 
(fast, slow, first). The space usage does not depend on the size of the input.

"""