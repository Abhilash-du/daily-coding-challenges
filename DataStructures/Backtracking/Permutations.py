# Problem Description
# Given an integer array A of size N denoting collection of numbers , return all possible permutations.
#
# NOTE:
# No two entries in the permutation sequence should be the same.
# For the purpose of this problem, assume that all the numbers in the collection are unique.
# Return the answer in any order
# WARNING: DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS.
# Example : next_permutations in C++ / itertools.permutations in python.
# If you do, we will disqualify your submission retroactively and give you penalty points.
#
# Problem Constraints: 1 <= N <= 9
#
# Input Format: Only argument is an integer array A of size N.
#
# Output Format
# Return a 2-D array denoting all possible permutation of the array.
#
# Example Input A = [1, 2, 3]
#
# Example Output
# [ [1, 2, 3]
#   [1, 3, 2]
#   [2, 1, 3]
#   [2, 3, 1]
#   [3, 1, 2]
#   [3, 2, 1] ]
#
# Example Explanation
# All the possible permutation of array [1, 2, 3].

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        ans = []

        def permute_internal(arr, start, n):
            if start == n:
                temp = arr.copy()
                ans.append(temp)
                return
            for i in range(start, n):
                # swap index
                arr[start], arr[i] = arr[i], arr[start]
                permute_internal(arr, start + 1, n)
                arr[start], arr[i] = arr[i], arr[start]

        permute_internal(A, 0, len(A))
        return ans

# Solution Approach/Observation:-
# So in order to find the permutations we will loop around the each element in given Array A
# We will freeze one index value(start) and then proceed further by doing permutation on the other index values
# recursively, once the index that swapped completes the length of the given array, means we have got the answer and
# we will append it
