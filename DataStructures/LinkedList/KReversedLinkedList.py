"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to find the K reversed linked list

Problem Description
Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and return the modified
linked list.

Problem Constraints
1 <= |A| <= 103
B always divides A

Input Format
The first argument of input contains a pointer to the head of the linked list.
The second arugment of input contains the integer, B.

Output Format
Return a pointer to the head of the modified linked list.

Example Input
Input 1:
 A = [1, 2, 3, 4, 5, 6]
 B = 2

Input 2:
 A = [1, 2, 3, 4, 5, 6]
 B = 3

Example Output
Output 1: [2, 1, 4, 3, 6, 5]
Output 2: [3, 2, 1, 6, 5, 4]

Example Explanation:-

Explanation 1:
 For the first example, the list can be reversed in groups of 2.
    [[1, 2], [3, 4], [5, 6]]
 After reversing the K-linked list
    [[2, 1], [4, 3], [6, 5]]

Explanation 2:
 For the second example, the list can be reversed in groups of 3.
    [[1, 2, 3], [4, 5, 6]]
 After reversing the K-linked list
    [[3, 2, 1], [6, 5, 4]]

"""


def reverseList(self, A, B):
    currNode = A  # Initialize the current node to the head of the linked list
    prevNode = None  # Initialize the previous node to None
    nextNode = None  # Initialize the next node to None
    node_count = 0  # Initialize a counter to keep track of the number of nodes reversed

    while currNode and node_count < B:
        nextNode = currNode.next  # Save the next node
        currNode.next = prevNode  # Reverse the link to the previous node
        prevNode = currNode  # Move the previous node to the current node
        currNode = nextNode  # Move the current node to the next node
        node_count += 1  # Increment the counter

    if currNode:
        A.next = self.reverseList(currNode, B)  # Recursively reverse the remaining linked list

    return prevNode  # Return the new head node of the reversed linked list


"""
Approach:
The reverseList method uses a recursive approach to reverse the linked list in groups of size B.
It iterates through the linked list, reversing B nodes at a time and recursively reversing the remaining list.
The method returns the head node of the modified linked list.

Time Complexity: O(N), where N is the number of nodes in the linked list.
The method visits each node once during the reversal process.

Space Complexity: O(1)
The method uses a constant amount of extra space to store pointers.
"""
