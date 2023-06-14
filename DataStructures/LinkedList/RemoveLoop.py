"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to break the loop in LinkedList

Problem Description
You are given a linked list that contains a loop.
You need to find the node, which creates a loop and break it by making the node point to NULL.

Problem Constraints
1 <= number of nodes <= 1000

Input Format
The first of the input contains a LinkedList, where the first number is the number of nodes N, and the next N nodes
are the node value of the linked list.
The second line of the input contains an integer which denotes the position of node where cycle starts.

Output Format
return the head of the updated linked list.

Example Input
Input 1:
1 -> 2
^    |
| - -

Input 2:
3 -> 2 -> 4 -> 5 -> 6
          ^         |
          |         |
          - - - - - -

Example Output
Output 1: 1 -> 2 -> NULL
Output 2: 3 -> 2 -> 4 -> 5 -> 6 -> NULL


Example Explanation:-
Explanation 1: Chain of 1->2 is broken.
Explanation 2: Chain of 4->6 is broken.

"""


# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, A):
        fast = A.next  # Move fast pointer 2 steps at a time
        slow = A  # Move slow pointer 1 step at a time
        flag = False  # Flag to indicate if loop is found

        while fast:
            fast = fast.next.next  # Move fast pointer 2 steps
            slow = slow.next  # Move slow pointer 1 step

            if fast == slow:  # If fast and slow pointers meet, loop is found
                flag = True
                break

        if flag:
            slow = A  # Reset slow pointer to the head of the list
            while fast.next != slow:  # Move fast and slow pointers at the same speed until they meet
                fast = fast.next
                slow = slow.next

            fast.next = None  # Break the loop by making the next of the last node in the loop as None

        return A  # Return the head of the updated linked list
"""
Approach:
The code uses Floyd's cycle detection algorithm to find and break the cycle in a linked list. 
It uses two pointers - slow and fast. The fast pointer moves two steps at a time, while the slow pointer moves one step 
at a time. If there is a cycle in the linked list, the fast and slow pointers will eventually meet. 
Once a cycle is detected, the algorithm finds the start point of the cycle by resetting the slow pointer to the head 
of the list and moving both pointers at the same speed until they meet again. Finally, the algorithm breaks the 
cycle by making the next of the last node in the cycle as None.

Time Complexity:
The algorithm runs in linear time, O(N), where N is the number of nodes in the linked list. 
It performs a single pass through the list to detect the cycle and find its start point.

Space Complexity:
The algorithm has a constant space complexity, O(1). It uses only two pointers to detect and break the cycle, 
without requiring any additional data structures.

"""