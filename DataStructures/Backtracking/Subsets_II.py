# Problem Description
# Given a collection of integers denoted by array A of size N that might contain duplicates,
# return all possible subsets.
#
# NOTE:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# The subsets must be sorted lexicographically.
#
#
# Problem Constraints
# 0 <= N <= 16
#
#
#
# Input Format
# Only argument is an integer array A of size N.
#
# Output Format
# Return a 2-D vector denoting all the possible subsets.
#
# Example Input
# Input 1:  A = [1, 2, 2]
# Input 2:  A = [1, 1]
#
# Example Output
# Output 1:
#  [
#     [],
#     [1],
#     [1, 2],
#     [1, 2, 2],
#     [2],
#     [2, 2]
#  ]
#
# Output 2:
#  [
#     [],
#     [1],
#     [1, 1]
#  ]
#
# Example Explanation
# Explanation 1: All the subsets of the array [1, 2, 2] in lexicographically sorted order.
class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        ans = []
        A.sort()
        n = len(A)

        def powerSet(arr, indx):
            if indx == n:
                ans.append(arr.copy())
                return
            arr.append(A[indx])
            powerSet(arr, indx + 1)

            while indx < n - 1 and A[indx] == A[indx + 1]:
                indx += 1

            arr.pop()
            powerSet(arr, indx + 1)

        powerSet([], 0)
        ans.sort()
        return ans
#
# Solution Approach/Observation:-
# Think in terms of recursion.
# This is very similar to the problem where you need to generate subsets for distinct integer.
# However, in this case, because of repetitions, things are not as simple as choosing or rejecting an element.
# Now for the elements which are repeated you need to iterate over the count of elements
# you are going to include in your subset.