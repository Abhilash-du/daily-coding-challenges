# Q1. Merge Two Sorted Arrays
# Problem Description
# Given two sorted integer arrays A and B, merge B and A as one sorted array and return it as an output.
#
# Problem Constraints
# -1010 <= A[i], B[i] <= 1010
#
# Input Format
# First Argument is a 1-D array representing A.
# Second Argument is also a 1-D array representing B.
#
# Output Format
# Return a 1-D vector which you got after merging A and B.
#
# Example Input
# Input 1:
# A = [4, 7, 9 ]
# B = [2, 11, 19 ]
#
# Input 2:
# A = [1]
# B = [2]
#
#
# Example Output
# Output 1: [2, 4, 7, 9, 11, 19]
# Output 2: [1, 2]
#
# Example Explanation
# Explanation 1: Merging A and B produces the output as described above.
# Explanation 2: Merging A and B produces the output as described above.
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a list of integers
    def solve(self, A, B):
        i, j, k = 0, 0, 0
        n1, n2 = len(A), len(B)
        merged_arr = [0 for _ in range(n1 + n2)]

        while i < n1 and j < n2:  # comparing and inserting in sorted manner
            if A[i] <= B[j]:
                merged_arr[k] = A[i]
                i += 1
            else:
                merged_arr[k] = B[j]
                j += 1
            k += 1

        if i < n1:  # checking in case i index has not covered all A indexes
            while i < n1:
                merged_arr[k] = A[i]  # adding pending values
                i += 1
                k += 1
        else:  # checking in case j index has not covered all B indexes
            while j < n2:
                merged_arr[k] = B[j]  # adding pending values
                j += 1
                k += 1
        return merged_arr

# Approach Followed/Observations:-
# Use of additional space is allowed. So, maybe you should try collecting the output in a separate array.
#
# Note: You need two pointers at the head of each array, and you need to compare the values at the head of the arrays
# to get the current minimum.
#
# Since A is sorted, all values after the pointer are going to be bigger.
# Since B is sorted, all values after the pointer are going to be bigger.
# All values before the pointer have already been put in the result array.
#
# Corner cases:
#
# What if pointer 1 reaches the end of the array first? What if pointer 2 reaches the end of the array first? If
# pointer 1 reaches the end we can just keep on putting the elements from B in the result array while the pointer 2
# does not reach the end. The same process goes for if pointer 2 reaches the end.
