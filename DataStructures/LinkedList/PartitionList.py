"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution partition two Linked lists such that all nodes less than B come before nodes greater than
            or equal to B.

Partition List
Given a linked list A and a value B, partition it such that all nodes less than B come before nodes greater than or
equal to B.

You should preserve the original relative order of the nodes in each of the two partitions.

Problem Constraints
1 <= |A| <= 106
1 <= A[i], B <= 109

Input Format
The first argument of input contains a pointer to the head to the given linked list.
The second argument of input contains an integer, B.

Output Format
Return a pointer to the head of the modified linked list.

Example Input
Input 1:
A = [1, 4, 3, 2, 5, 2]
B = 3

Input 2:
A = [1, 2, 3, 1, 3]
B = 2

Example Output
Output 1:[1, 2, 2, 4, 3, 5]
Output 2:[1, 1, 2, 3, 3]

Example Explanation
Explanation 1:  [1, 2, 2] are less than B wheread [4, 3, 5] are greater than or equal to B.
Explanation 2: [1, 1] are less than B wheread [2, 3, 3] are greater than or equal to B.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # Function to partition the linked list based on a given value B
    # @param head: head node of the linked list
    # @param B: partition value
    # @return: head node of the modified linked list
    def partitionLinkedList(self, head, B):
        # Initialize two dummy nodes to create two separate linked lists:
        # one for nodes with values less than B and the other for values greater than or equal to B.
        smaller_dummy = ListNode(0)  # Dummy node for smaller values
        smaller_tail = smaller_dummy  # Pointer to the tail of the smaller values list

        greater_equal_dummy = ListNode(0)  # Dummy node for greater or equal values
        greater_equal_tail = greater_equal_dummy  # Pointer to the tail of the greater or equal values list

        current = head  # Initialize a pointer to traverse the input linked list

        # Traverse through the input linked list
        while current:
            if current.val < B:
                # If the current node's value is less than B, add it to the smaller values list
                smaller_tail.next = current
                smaller_tail = smaller_tail.next
            else:
                # If the current node's value is greater than or equal to B,
                # add it to the greater or equal values list
                greater_equal_tail.next = current
                greater_equal_tail = greater_equal_tail.next

            current = current.next  # Move to the next node

        # Close the two partitioned lists by setting their last nodes' next pointers to None
        greater_equal_tail.next = None

        # Connect the smaller values list to the greater or equal values list
        smaller_tail.next = greater_equal_dummy.next

        # Return the head of the modified linked list, which is the second node of the smaller values list
        return smaller_dummy.next


"""
# Intuition:
We use two separate linked lists to keep track of nodes with values less than B
and nodes with values greater than or equal to B. As we traverse the input list,
we place nodes into these two lists based on their values. Finally, we connect
the tail of the smaller values list to the head of the greater or equal values list.

# Time Complexity (TC):
The algorithm iterates through the entire input linked list exactly once,
so the time complexity is O(N), where N is the number of nodes in the linked list.

# Space Complexity (SC):
We are using two extra linked lists to partition the input list. In the worst case,
all nodes can have values less than B or all nodes can have values greater than B,
which means we would use additional space proportional to the input size.
Therefore, the space complexity is O(N), where N is the number of nodes in the linked list.
"""
