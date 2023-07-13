"""
Q2. Sort List
Problem Description
Sort a linked list, A in O(n log n) time.

Problem Constraints
0 <= |A| = 10^5

Input Format
The first and the only arugment of input contains a pointer to the head of the linked list, A.

Output Format
Return a pointer to the head of the sorted linked list.

Example Input:-
Input 1: A = [3, 4, 2, 8]
Input 2: A = [1]


Example Output:-
Output 1: [2, 3, 4, 8]
Output 2: [1]

Example Explanation:-
Explanation 1: The sorted form of [3, 4, 2, 8] is [2, 3, 4, 8].
Explanation 2: The sorted form of [1] is [1].

"""


class Solution:
    def sortList(self, head):
        # Base case: empty list or single node
        if head is None or head.next is None:
            return head

        # Find the middle of the linked list using slow and fast pointers
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        # Recursively sort the two halves
        left = self.sortList(head)
        right = self.sortList(slow)

        # Merge the sorted halves back together
        def mergeLists(left_head, right_head):
            # If either list is empty, return the other list
            if left_head is None:
                return right_head
            if right_head is None:
                return left_head

            # Determine the head of the merged list
            merged_head = left_head if left_head.val < right_head.val else right_head

            # Initialize pointers for merging
            prev = None
            current = merged_head

            # Merge the two lists by rearranging pointers
            while left_head and right_head:
                if left_head.val < right_head.val:
                    prev = left_head
                    left_head = left_head.next
                else:
                    node_to_merge = right_head
                    right_head = right_head.next
                    if prev:
                        prev.next = node_to_merge
                        node_to_merge.next = left_head
                        prev = node_to_merge
                    else:
                        prev = node_to_merge
                        prev.next = left_head

            # Attach the remaining nodes from the non-empty list
            if right_head:
                prev.next = right_head

            return merged_head

        # Return the merged and sorted list
        return mergeLists(left, right)


"""
Intuition:
The solution uses the merge sort algorithm to sort the linked list.
The merge sort algorithm follows a divide-and-conquer approach:
1. The list is divided into two halves by finding the middle element using slow and fast pointers.
2. The two halves are recursively sorted using the same merge sort function.
3. The sorted halves are merged back together by comparing the values of the nodes.
4. The merge process continues until the entire list is sorted.

Time Complexity:
The time complexity of this approach is O(n log n), where n is the number of nodes in the linked list.
This is because the list is divided into halves recursively until each sublist has only one node,
and the merge process takes O(n) time in each recursion. Hence, the overall time complexity is O(n log n).

Space Complexity:
The space complexity is O(log n) due to the recursive calls to sort the list.
The recursion depth is log n since the list is divided into halves at each recursive call.
Additionally, the merge process takes O(1) space as it rearranges the existing nodes.
Therefore, the overall space complexity is dominated by the recursion depth, resulting in O(log n).
"""
