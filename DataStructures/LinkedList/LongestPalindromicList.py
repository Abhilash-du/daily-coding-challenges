"""
# Author: Abhilash Dubey
# Problem Statement: Given a linked list of integers, find and return the length of the longest palindrome list that
                    exists in that linked list.
# GitHub: https://github.com/Abhilash-du/


Q4. Longest Palindromic List
Problem Description
Given a linked list of integers. Find and return the length of the longest palindrome list that exists in that linked list.
A palindrome list is a list that reads the same backward and forward.
Expected memory complexity : O(1)

Problem Constraints
1 <= length of the linked list <= 2000
1 <= Node value <= 100

Input Format
The only argument given is head pointer of the linked list.

Output Format
Return the length of the longest palindrome list.

Example Input:-
Input 1:   2 -> 3 -> 3 -> 3
Input 2:   2 -> 1 -> 2 -> 1 ->  2 -> 2 -> 1 -> 3 -> 2 -> 2

Example Output:-
Output 1: 3
Output 2: 5

Example Explanation:-
Explanation 1:  3 -> 3 -> 3 is largest palindromic sublist
Explanation 2:  2 -> 1 -> 2 -> 1 -> 2 is largest palindromic sublist.
"""


class Solution:
    def getPalindromeLength(self, node1, node2):
        """
        Helper function to calculate the length of a palindrome sublist.
        It takes two nodes as input and returns the length of the palindrome sublist.
        """
        length = 0
        while node1 and node2 and node1.val == node2.val:
            node1 = node1.next
            node2 = node2.next
            length += 2
        return length

    def longestPalindrome(self, A):
        """
        Function to find the length of the longest palindrome sublist in a linked list.
        It takes the head pointer of the linked list as input and returns the length of the longest palindrome sublist.
        """
        if not A or not A.next:
            return 1 if A else 0

        reverse = A  # Points to the reversed sublist
        forward = A.next  # Points to the next node
        prev = None  # Points to the previous node of 'reverse'
        longest_length = 1  # Length of the longest palindrome sublist

        while forward:
            # Check for even-length palindrome sublist
            reverse.next = prev
            even_length = self.getPalindromeLength(reverse, forward)
            longest_length = max(longest_length, even_length)

            # Check for odd-length palindrome sublist
            odd_length = self.getPalindromeLength(reverse, forward.next)
            longest_length = max(longest_length, odd_length + 1)

            # Move pointers forward
            prev = reverse
            reverse = forward
            forward = forward.next

        return longest_length


"""
Intuition:
- We can solve this problem using two pointers technique.
- Start with two pointers, 'reverse' and 'forward', initially pointing to the first and second nodes of the linked list, respectively.
- At each step, we compare the values of 'reverse' and 'forward' nodes. If they are equal, it means we have found a potential palindrome sublist.
- We keep moving both pointers forward until the values are not equal or we reach the end of the linked list.
- After finding the potential palindrome sublist, we update the 'longest_length' variable with the maximum length found so far.
- We repeat the process for even-length and odd-length palindrome sublists by considering the next node of 'forward'.
- Finally, we return the 'longest_length' as the result.

Time Complexity (TC):
- The algorithm iterates through the linked list once, comparing the values of nodes.
- Hence, the time complexity is O(N), where N is the length of the linked list.

Space Complexity (SC):
- The algorithm uses a constant amount of extra space to store pointers and variables.
- Therefore, the space complexity is O(1).
"""
