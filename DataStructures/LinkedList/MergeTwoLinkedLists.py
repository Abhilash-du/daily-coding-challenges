"""
# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to Merge Two Sorted Linked Lists

Problem Description
Merge two sorted linked lists, A and B, and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists and should also be sorted.

Problem Constraints
0 <= |A|, |B| <= 105

Input Format
The first argument of input contains a pointer to the head of linked list A.
The second argument of input contains a pointer to the head of linked list B.

Output Format
Return a pointer to the head of the merged linked list.

Example Input:-
Input 1:
 A = 5 -> 8 -> 20
 B = 4 -> 11 -> 15

Input 2:-
 A = 1 -> 2 -> 3
 B = Null

Example Output
Output 1: 4 -> 5 -> 8 -> 11 -> 15 -> 20
Output 2: 1 -> 2 -> 3

Example Explanation:-
Explanation 1: Merging A and B will result in 4 -> 5 -> 8 -> 11 -> 15 -> 20
Explanation 2: We don't need to merge as B is empty.

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, A, B):
        # Initialize pointers for both lists
        p1, p2 = A, B

        # Create a dummy node as the starting point of the merged list
        curr = ListNode(0)
        # Save the head of the merged list for returning at the end
        head = curr

        # Traverse both lists until one of them reaches the end
        while p1 and p2:
            # Compare the values of the current nodes from both lists
            if p1.val < p2.val:
                # Connect the current node of list A to the merged list
                curr.next = p1
                # Move the pointer of list A to the next node
                p1 = p1.next
            else:
                # Connect the current node of list B to the merged list
                curr.next = p2
                # Move the pointer of list B to the next node
                p2 = p2.next

            # Move the current pointer of the merged list to the next node
            curr = curr.next

        # Append the remaining nodes of list A, if any
        if p1:
            curr.next = p1

        # Append the remaining nodes of list B, if any
        if p2:
            curr.next = p2

        # Return the head of the merged list
        return head.next


"""
Intuition:
To merge two sorted linked lists, we can use a simple iterative approach. We initialize two pointers, p1 and p2, 
pointing to the heads of the two lists A and B, respectively. 
We also create a dummy node, curr, to build the merged list.

Then, we compare the values of the current nodes pointed by p1 and p2. 
We connect the smaller value to the curr node and move the corresponding pointer forward. 
We repeat this process until one of the lists reaches the end.

After the loop, we check if any list still has remaining nodes and append them to the merged list. 

Finally, we return the head of the merged list.

Time Complexity:
The time complexity of this approach is O(N + M), where N and M are the lengths of the input linked lists A and B, 
respectively. We traverse both lists simultaneously, comparing and merging the nodes. 
The time complexity is linear with respect to the total number of nodes in the merged list.

Space Complexity:
The space complexity of this approach is O(1) since we are not using any additional data structures that scale with the 
input size. We only use a constant amount of extra space to store the pointers and the dummy node.
"""
