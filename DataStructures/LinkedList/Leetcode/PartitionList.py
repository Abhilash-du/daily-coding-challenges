"""
86. Partition List
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater
than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:
Input: head = [2,1], x = 2
Output: [1,2]

Constraints:
The number of nodes in the list is in the range [0, 200].
-100 <= Node.val <= 100
-200 <= x <= 200
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def partition(self, head, x):
        # Initialize two dummy nodes to build separate lists for values less than x (smaller) and greater than x (
        # larger)
        larger = ListNode()
        larger_head = larger  # Keep a reference to the head of the larger list
        smaller = ListNode()
        smaller_head = smaller  # Keep a reference to the head of the smaller list

        curr = head

        while curr:
            if curr.val >= x:
                # Append the current node to the larger list
                larger.next = curr
                larger = larger.next
            else:
                # Append the current node to the smaller list
                smaller.next = curr
                smaller = smaller.next
            curr = curr.next

        # Terminate both smaller and larger lists
        larger.next = None
        smaller.next = larger_head.next  # Connect the smaller list to the larger list

        return smaller_head.next  # Return the head of the modified linked list

"""
Intuition:
This solution aims to partition a linked list by rearranging its nodes such that all nodes with values less than the 
given value 'x' come before nodes with values greater than or equal to 'x'. It iterates through the original list, 
maintaining two separate linked lists, one for values less than 'x' and another for values greater than or equal to 'x'.
 After the traversal, the smaller list is connected to the larger list to maintain the original order of elements.

Time Complexity:
The algorithm iterates through the entire linked list once, which takes O(n) time, where 'n' is the number of nodes in 
the list.

Space Complexity:
The algorithm utilizes two additional linked lists, one for values less than 'x' and another for values greater than or
 equal to 'x'. Therefore, the space complexity is O(n), where 'n' is the number of nodes in the list.
"""