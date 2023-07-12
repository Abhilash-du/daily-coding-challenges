"""
# Author: Abhilash Dubey
# Problem Statement: Given a linked list of integers, find if its a palindrome
# GitHub: https://github.com/Abhilash-du
#
Problem Description
Given a singly linked list A, determine if it's a palindrome. Return 1 or 0, denoting if it's a palindrome or not,
respectively.

Problem Constraints
1 <= |A| <= 10^5

Input Format
The first and the only argument of input contains a pointer to the head of the given linked list.

Output Format
Return 0, if the linked list is not a palindrome.
Return 1, if the linked list is a palindrome.

Example Input
Input 1:A = [1, 2, 2, 1]
Input 2:A = [1, 3, 2]

Example Output
Output 1: 1
Output 2: 0

Example Explanation:-
Explanation 1: The first linked list is a palindrome as [1, 2, 2, 1] is equal to its reversed form.
Explanation 2: The second linked list is not a palindrom as [1, 3, 2] is not equal to [2, 3, 1].
"""
class Solution:
    def isPalindrome(self, head):
        # Initialize two pointers, slow and fast, pointing to the head of the linked list
        slow = fast = head

        # Move slow pointer one step and fast pointer two steps at a time until fast reaches the end of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list starting from the next of the mid node
        curr = slow
        prev = None
        while curr:
            next_node = curr.next  # Store the next node in the temporary variable
            curr.next = prev  # Reverse the link of the current node
            prev = curr  # Update the previous node to the current node
            curr = next_node  # Move to the next node

        # Check if the first half of the original linked list and the reversed second half are identical
        first_half = head
        second_half = prev
        while second_half and first_half:
            if second_half.val != first_half.val:
                return 0  # Not a palindrome, return 0
            second_half = second_half.next
            first_half = first_half.next

        return 1  # Palindrome, return 1


"""
Intuition:
The algorithm uses the concept of the runner technique to find the middle node of the linked list.
 It then reverses the second half of the linked list and compares the values of the first half with the reversed 
 second half to check if it's a palindrome.

Time Complexity: 
The algorithm requires traversing the linked list to find the middle node, which takes O(N/2) time. 
Reversing the second half of the list also takes O(N/2) time. Finally, comparing the values of the first half with 
the reversed second half takes O(N/2) time. Therefore, the overall time complexity is O(N).

Space Complexity: 
The algorithm only uses a constant amount of extra space, regardless of the size of the input.
Hence, the space complexity is O(1).

"""
