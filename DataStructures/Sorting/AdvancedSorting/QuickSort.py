# Author: Abhilash Dubey
# GitHub:  https://github.com/Abhilash-du/
# Description: Python solution to sort the array using QuickSort.

"""
Problem Description
Given an integer array A, sort the array using QuickSort.

Problem Constraints
1 <= |A| <= 105
1 <= A[i] <= 109

Input Format
First argument is an integer array A.

Output Format
Return the sorted array.

Example Input
Input 1: A = [1, 4, 10, 2, 1, 5]
Input 2: A = [3, 7, 1]

Example Output
Output 1: [1, 1, 2, 4, 5, 10]
Output 2: [1, 3, 7]

Example Explanation
Explanation 1: Return the sorted array.
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        # Helper function to partition the array
        def partition(left, right):
            # Choose the pivot element (in this case, the leftmost element)
            pivot = A[left]
            l = left
            r = right

            while l < r:
                # Find an element from the left that is greater than the pivot
                while l <= r and A[l] <= pivot:
                    l += 1
                # Find an element from the right that is less than or equal to the pivot
                while l <= r and A[r] > pivot:
                    r -= 1
                if l < r:
                    # Swap the elements to put them in the correct partition
                    A[l], A[r] = A[r], A[l]

            # Swap the pivot element into its correct position
            A[left], A[r] = A[r], A[left]
            return r

        # Helper function to perform quicksort
        def quickSort(left, right):
            if left >= right:
                return  # Base case: array of size 1 or empty

            # Partition the array and get the pivot index
            pivot = partition(left, right)

            # Recursively sort the subarrays on both sides of the pivot
            quickSort(left, pivot - 1)
            quickSort(pivot + 1, right)

        # Call the quicksort function on the entire array
        quickSort(0, len(A) - 1)

        # Return the sorted array
        return A

"""
Intuition:

The QuickSort algorithm works by selecting a pivot element from the array and partitioning the other elements into two
 sub-arrays according to whether they are less than or greater than the pivot. The sub-arrays are then recursively 
 sorted. The key intuition behind QuickSort is the efficient partitioning of elements around a pivot, which divides 
 the problem into smaller sub-problems.

Choose a Pivot: Select a pivot element from the array. In this implementation, we choose the leftmost element as the
 pivot.

Partitioning: Rearrange the elements in the array such that all elements less than or equal to the pivot are on the left
 side, and all elements greater than the pivot are on the right side. The pivot is now in its final sorted position.

Recursion: Recursively apply the QuickSort algorithm to the left and right sub-arrays.

Base Case: The base case for the recursion is when the sub-array has only one element or is empty, as such arrays are
 already sorted.

Time Complexity (TC):

The time complexity of QuickSort is generally O(n log n) on average, where 'n' is the number of elements in the array.
In the worst case (unbalanced partitioning), it can be O(n^2).
The choice of pivot and the partitioning strategy can impact the time complexity.
In practice, QuickSort is often faster than other O(n log n) algorithms like MergeSort due to its low constant factors.
Space Complexity (SC):

The space complexity of QuickSort is O(log n) for the recursive call stack.
In the worst case (unbalanced partitioning), it can be O(n) for the stack.
The space complexity for the additional memory used during the partitioning process is O(1), as it sorts in-place 
without requiring additional data structures.
"""