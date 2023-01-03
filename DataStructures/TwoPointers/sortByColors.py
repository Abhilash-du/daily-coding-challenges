# Problem Description:
# Given an array with N objects colored red, white, or blue, sort them so that objects of the
# same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent red, white, and blue, respectively.
# Note: Using the library sort function is not allowed.
#
# Problem Constraints
# 1 <= N <= 1000000
# 0 <= A[i] <= 2
#
# Input Format
# First and only argument of input contains an integer array A.
#
# Output Format
# Return an integer array in asked order
#
# Example Input
# Input 1 : A = [0 1 2 0 1 2]
# Input 2:  A = [0]
#
# Example Output
# Output 1:  [0 0 1 1 2 2]
# Output 2:  [0]
#
# Example Explanation
# Explanation 1: [0 0 1 1 2 2] is the required order.

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def sortColors(self, A):
        low = 0
        high = len(A) - 1
        mid = 0

        while mid <= high:
            midVal = A[mid]
            if midVal == 0:
                A[low], A[mid] = A[mid], A[low]
                mid += 1
                low += 1
            if midVal == 1:
                mid += 1
            if midVal == 2:
                A[high], A[mid] = A[mid], A[high]
                high -= 1
        return A

# Solution Approach/ Observation:-
# There are multiple approaches possible here. We need to make sure we do not allocate extra memory.
#
# Approach 1:
#
# Count the number of red, white, and blue balls.
# Then, in another pass, set the initial redCount number of cells as
# 0, next whiteCount cell as 1, and next blueCount cells as 2. Requires two passes of the array.
#
# Approach 2:
#
# Swap the 0s to the start of the array maintaining a pointer, and 2s to the end of the array.
# 1s will automatically be in their right position.
