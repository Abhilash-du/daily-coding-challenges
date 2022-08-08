# Problem Description
# Given an array of integers A, find and return whether the given array contains a non-empty subarray
# with a sum equal to 0. If the given array contains a sub-array with sum zero return 1, else return 0.
#
# Problem Constraints
# 1 <= |A| <= 100000
# -10^9 <= A[i] <= 10^9
#
# Input Format: The only argument given is the integer array A.
#
# Output Format
# Return whether the given array contains a subarray with a sum equal to 0.
#
# Example Input
# Input 1: A = [1, 2, 3, 4, 5]
# Input 2: A = [-1, 1]
#
# Example Output
# Output 1:  0
# Output 2:  1
#
# Example Explanation
# Explanation 1: No subarray has sum 0.
# Explanation 2: The array has sum 0.
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)

        ps = 0
        hmap_index = {0: -1}  # hashmap to store prefix sum

        for i in range(0, n):
            ps += A[i]
            if ps in hmap_index.keys():  # checking if hashmap has repeating key
                return 1
            else:
                hmap_index[ps] = i
        return 0

# For execution
# A = [1, 2, 3, 4, 5]
# zeroSumCheck = Solution()
# print(zeroSumCheck.solve(A))

# Observation/Approach:-
# The idea is to iterate through the array, and for every element A[i],
# calculate sum of elements from 0 to i (this can simply be done as sum += arr[i]).
#
# If the current sum has been seen before, then there is a zero-sum array.
#
# Hashing is used to store the sum values so that we can quickly store sum and
# find out whether the current sum is seen before or not.
