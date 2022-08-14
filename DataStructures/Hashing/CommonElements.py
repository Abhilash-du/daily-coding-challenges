# Problem Description
# Given two integer arrays, A and B of size N and M, respectively. Your task is to find all the common elements
# in both the array.
#
# NOTE:
# Each element in the result should appear as many times as it appears in both arrays.
# The result can be in any order.
#
# Problem Constraints
# 1 <= N, M <= 105
# 1 <= A[i] <= 109
#
# Input Format
# First argument is an integer array A of size N.
# Second argument is an integer array B of size M.
#
# Output Format
# Return an integer array denoting the common elements.
#
# Example Input
# Input 1:
#  A = [1, 2, 2, 1]
#  B = [2, 3, 1, 2]
#
# Input 2:
#  A = [2, 1, 4, 10]
#  B = [3, 6, 2, 10, 10]
#
# Example Output
# Output 1: [1, 2, 2]
# Output 2: [2, 10]
#
# Example Explanation
# Explanation 1:  Elements (1, 2, 2) appears in both the array. Note 2 appears twice in both the array.
# Explanation 2:  Elements (2, 10) appears in both the array.

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        hmap_A = {}
        for i in A:
            if i in hmap_A.keys():
                hmap_A[i] = hmap_A.get(i) + 1
            else:
                hmap_A[i] = 1
        C = []
        for i in B:
            if i in hmap_A.keys():
                if hmap_A[i] > 0:
                    C.append(i)
                    hmap_A[i] = hmap_A.get(i) - 1
        return C

# Approaches followed:0
# Approach 1:
#
# Use a HashMap to store the first array, then check each second array element and see if it is in the map.
# Note that since we need to output all repeated elements, we also need to count the occurrence of each array
# element in the map and consume it when we compare it with the second array.
#
# Time Complexity: O(N+M)
# Space Complexity: O(min(N, m))
#
# Approach 2:
# Sort the two arrays and iterate over to find out the intersections. So the overall time complexity
# is bounded by O(n logn), where n is the length of the longer array.
# The main body of the loop is bounded by O(m + n).
