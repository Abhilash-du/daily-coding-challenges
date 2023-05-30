"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to remove the B-th node from Linkedlist

Problem Description
Given a linked list A, remove the B-th node from the end of the list and return its head. F
or example, Given linked list: 1->2->3->4->5, and B = 2. After removing the second node from the end, the linked list
becomes 1->2->3->5.
NOTE: If B is greater than the size of the list, remove the first node of the list. NOTE: Try doing it using constant
 additional space.

Problem Constraints
1 <= |A| <= 106

Input Format
The first argument of input contains a pointer to the head of the linked list. The second argument of input contains
 the integer B.

Output Format
Return the head of the linked list after deleting the B-th element from the end.

Example Input
Input 1:
A = 1->2->3->4->5
B = 2

Input 2:
A = 1
B = 1

Example Output
Output 1:  1->2->3->5
Output 2:

Example Explanation:-
Explanation 1: In the first example, 4 is the second last element.
Explanation 2: In the second example, 1 is the first and the last element.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        fast = A  # Pointer to move B positions ahead
        count = 0

        # Move the 'fast' pointer B positions ahead
        for i in range(B):
            fast = fast.next
            if not fast:
                return A.next  # If 'fast' reaches the end, remove the head

        prev = None  # Pointer to the previous node of 'slow'
        slow = A  # Pointer to find the B-th node from the end

        # Move 'fast' and 'slow' pointers simultaneously
        while fast:
            fast = fast.next
            prev = slow
            slow = slow.next

        prev.next = slow.next  # Skip over the B-th node by updating 'next' reference

        return A


"""
Intuition
To solve this problem efficiently, we can use the two-pointer technique. By maintaining a `fast` and `slow` pointer, 
we can find the desired node and remove it from the list.

Complexity Analysis
Time Complexity: O(N), where N is the number of nodes in the linked list. 
We traverse the list twice, once with the fast pointer and once with the slow pointer.
Space Complexity: O(1), as we only use a constant amount of extra space.
"""