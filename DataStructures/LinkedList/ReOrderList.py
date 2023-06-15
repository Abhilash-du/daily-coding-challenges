"""
Q3. Reorder List
Problem Description
Given a singly linked list A  :-
 A: A0 → A1 → … → An-1 → An
reorder it to:

 A0 → An → A1 → An-1 → A2 → An-2 → …
You must do this in-place without altering the nodes' values.

Problem Constraints
1 <= |A| <= 106

Input Format
The first and the only argument of input contains a pointer to the head of the linked list A.

Output Format
Return a pointer to the head of the modified linked list.

Example Input
Input 1: A = [1, 2, 3, 4, 5]
Input 2: A = [1, 2, 3, 4]

Example Output
Output 1: [1, 5, 2, 4, 3]
Output 2: [1, 4, 2, 3]


Example Explanation:-
Explanation 1: The array will be arranged to [A0, An, A1, An-1, A2].
Explanation 2: The array will be arranged to [A0, An, A1, An-1, A2].
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        # Find the middle node of the linked list
        slow = A
        fast = A.next

        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break
        mid_node = slow

        # Reverse the second half of the linked list
        temp = slow.next
        mid_node.next = None

        prev = None
        curr = temp
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        grp1_node = A
        grp2_node = prev

        # Reorder the linked list by alternating nodes from the first and second halves
        while grp1_node and grp2_node:
            first = grp1_node.next
            grp1_node.next = grp2_node
            second = grp2_node.next
            grp2_node.next = first
            grp2_node = second
            grp1_node = first

        return A
"""
Intuition:
The approach involves three steps:
1. Finding the middle node of the linked list using the slow and fast pointer technique.
2. Reversing the second half of the linked list.
3. Reordering the linked list by alternating nodes from the first and second halves.

Time Complexity: The time complexity of this approach is O(N), where N is the number of nodes in the linked list. 
The finding the middle node takes O(N/2) time, reversing the second half takes O(N/2) time, and reordering 
the linked list takes O(N/2) time. However, the constants cancel out, resulting in an overall time complexity of O(N).

Space Complexity: The space complexity is O(1) as the reordering is done in-place without using any extra space.
"""